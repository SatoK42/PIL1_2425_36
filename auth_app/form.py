# auth_app/form.py
from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from phonenumbers import parse as pn_parse, is_valid_number, format_number, PhoneNumberFormat
from phonenumbers.phonenumber import PhoneNumber as PNType
from django.contrib.auth import authenticate


from .models import Users

ROLE_CHOICES = [
    ('conducteur', 'Conducteur'),
    ('passager', 'Passager'),
]

class UserModelForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Nom'}),
            'last_name':  forms.TextInput(attrs={'class':'form-control','placeholder':'Prénoms'}),
            'email':      forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control','id':'phone','placeholder':'Téléphone'}),
            'role': forms.Select(attrs={'class':'form-control'}),
        }

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p1 != p2:
            raise ValidationError("Les mots de passe ne correspondent pas.")
        return p2

    def clean_phone_number(self):
        raw = self.cleaned_data.get('phone_number')
        # Si c'est déjà un objet PhoneNumber (issu du model/django-phonenumber-field), on le réutilise
        if isinstance(raw, PNType):
            phone = raw
        else:
            # raw est une str : on précise éventuellement la région par défaut (e.g. 'BJ')
            try:
                phone = pn_parse(raw, 'BJ')
            except Exception:
                raise ValidationError("Format de numéro non reconnu.")
        # Puis on valide
        if not is_valid_number(phone):
            raise ValidationError("Numéro non valide.")
        # On retourne la version E.164
        return format_number(phone, PhoneNumberFormat.E164)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # on hache le mot de passe avant sauvegarde
        user.password = make_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EmailOrPhoneAuthenticationForm(forms.Form):
    login     = forms.CharField(label="Email ou téléphone", widget=forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Email ou téléphone'}))
    password  = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
                    attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    user_cache = None

    def clean(self):
        data = self.cleaned_data
        login    = data.get('login')
        password = data.get('password')
        if login and password:
            # passe les deux dans authenticate(); votre backend décidera
            user = authenticate(username=login, password=password)
            if user is None:
                raise forms.ValidationError("Identifiant ou mot de passe invalide.")
            if not user.is_active:
                raise forms.ValidationError("Compte inactif.")
            self.user_cache = user
        return data

    def get_user(self):
        return self.user_cache