from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'photo',
            'is_driver',
            'vehicle_type',
            'seats',
            'brand',
            'model',
            'departure_time',
            'departure_lat',
            'departure_lng',
        ]
        widgets = {
            'is_driver': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'id_is_driver'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-select', 'id': 'id_vehicle_type'}),
            'seats': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'id': 'id_seats'}),
            'brand': forms.TextInput(attrs={'class': 'form-input', 'id': 'id_brand'}),
            'model': forms.TextInput(attrs={'class': 'form-input', 'id': 'id_model'}),
            'departure_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-input', 'id': 'id_departure_time'}),
            'departure_lat': forms.HiddenInput(attrs={'id': 'id_departure_lat'}),
            'departure_lng': forms.HiddenInput(attrs={'id': 'id_departure_lng'}),
        }

    def clean(self):
        cleaned = super().clean()
        is_driver = cleaned.get('is_driver')
        vehicle_type = cleaned.get('vehicle_type')
        seats = cleaned.get('seats')

        if is_driver:
            if not vehicle_type:
                self.add_error('vehicle_type', "Veuillez préciser le type de véhicule.")
            if seats is None:
                self.add_error('seats', "Veuillez préciser le nombre de places.")
            elif seats < 1:
                self.add_error('seats', "Le nombre de places doit être au moins 1.")
        else:
            # S’assurer qu’on ne garde pas d’anciennes valeurs incohérentes si is_driver=False
            cleaned['vehicle_type'] = None
            cleaned['seats'] = None
            cleaned['brand'] = ''
            cleaned['model'] = ''

        # Trajet quotidien : si l’utilisateur donne heure mais pas coord, ou vice versa, on peut choisir de valider partiellement.
        # Ici on autorise vide ; si lat/lng fournis sans time, on accepte ; ou time sans lat/lng, mais on peut avertir.
        dep_time = cleaned.get('departure_time')
        lat = cleaned.get('departure_lat')
        lng = cleaned.get('departure_lng')
        if (lat is not None or lng is not None) and not (lat is not None and lng is not None):
            # cas où seul l’un des deux est fourni
            self.add_error(None, "Veuillez spécifier à la fois latitude et longitude du point de départ.")
        return cleaned

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si instance existante et is_driver=False, masquer les champs véhicule
        #if self.instance and not self.instance.is_driver:
        #    for fname in ['vehicle_type', 'seats', 'brand', 'model']:
        #        self.fields[fname].widget.attrs['style'] = 'display:none;'

        # Si instance a une coordonnée existante, on peut laisser le champ caché (lat/lng hidden) et géré par JS
        # departure_lat/lng sont cachés; pas besoin de widget visible.
