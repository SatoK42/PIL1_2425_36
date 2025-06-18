from django import forms
from .models import Trajet
from django.core.exceptions import ValidationError

class TrajetForm(forms.ModelForm):
    MODE_CHOICES = [
        ('quotidien', 'Trajet quotidien'),
        ('ponctuel', 'Trajet ponctuel'),
    ]
    mode = forms.ChoiceField(choices=MODE_CHOICES, widget=forms.RadioSelect)
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Date du trajet (obligatoire pour trajet ponctuel)."
    )
    heure = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
        help_text="Heure de départ (obligatoire pour trajet ponctuel)."
    )
    latitude_depart = forms.FloatField(widget=forms.HiddenInput(), required=False)
    longitude_depart = forms.FloatField(widget=forms.HiddenInput(), required=False)
    commentaire = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Trajet
        fields = ['mode', 'date', 'heure', 'latitude_depart', 'longitude_depart', 'commentaire']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # Par défaut si form non lié
        if not self.is_bound:
            self.fields['mode'].initial = 'quotidien'
        # Ajuster required selon mode actuel
        if self.is_bound:
            mode = self.data.get('mode')
        else:
            mode = self.fields['mode'].initial
        if mode == 'ponctuel':
            self.fields['date'].required = True
            self.fields['heure'].required = True
        else:
            self.fields['date'].required = False
            self.fields['heure'].required = False

    def clean(self):
        cleaned = super().clean()
        raw_mode = cleaned.get('mode')
        mode = raw_mode if raw_mode in ('quotidien', 'ponctuel') else 'quotidien'
        cleaned['mode'] = mode

        # Si quotidien, indiquer à l'instance qu'il s'agit d'un trajet récurrent
        if mode == 'quotidien':
            # Forcer recurring=True pour que model.clean ne réclame pas de date
            self.instance.recurring = True
            # Éviter toute date résiduelle
            self.instance.date = None
        else:
            # Ponctuel : on ne touche pas encore à instance.date ici, mais model.clean exigera date non None
            self.instance.recurring = False

        if mode == 'ponctuel':
            date = cleaned.get('date')
            heure = cleaned.get('heure')
            lat = cleaned.get('latitude_depart')
            lng = cleaned.get('longitude_depart')
            if date is None:
                raise ValidationError("Veuillez fournir la date pour le trajet ponctuel.")
            if heure is None:
                raise ValidationError("Veuillez fournir l'heure pour le trajet ponctuel.")
            if lat is None or lng is None:
                raise ValidationError("Veuillez sélectionner un point de départ sur la carte pour le trajet ponctuel.")
        # pour quotidien, pas d’autre validation de date/heure
        return cleaned
    
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        profile = user.profile
        instance.role = 'conducteur' if profile.is_driver else 'passager'
        mode = self.cleaned_data.get('mode') or 'quotidien'
        if mode == 'quotidien':
            instance.recurring = True
            instance.date = None
            if profile.departure_lat is None or profile.departure_lng is None or profile.departure_time is None:
                raise ValidationError("Votre profil doit contenir heure et coordonnées de départ pour trajet quotidien.")
            instance.latitude_depart = profile.departure_lat
            instance.longitude_depart = profile.departure_lng
            instance.heure = profile.departure_time
            # Fournir un lieu_depart générique ou depuis profil
            instance.lieu_depart = getattr(profile, 'address', 'Point habituel')
        else:
            instance.recurring = False
            instance.date = self.cleaned_data.get('date')
            instance.heure = self.cleaned_data.get('heure')
            instance.latitude_depart = self.cleaned_data.get('latitude_depart')
            instance.longitude_depart = self.cleaned_data.get('longitude_depart')
            instance.lieu_depart = "Coordonnées sélectionnées"
        if profile.is_driver:
            instance.nb_places = profile.seats
        else:
            instance.nb_places = None
        instance.user = user
        if commit:
            instance.save()
        return instance
