from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.widgets import TextInput

ROLE_CHOICES = [
    ('conducteur', 'Conducteur'),
    ('passager', 'Passager'),
]

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénoms'})
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'})
    )
    phone_number = PhoneNumberField(
        max_length=15,
        required=True,
        widget=PhoneNumberPrefixWidget(
            widgets=[TextInput()],
            attrs={'class': 'form-control', 'placeholder': 'Ex: 0700000000'}
        ),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Mot de passe',
            'autocomplete': 'new-password'
        })
    )
    confirm_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Confirmer le mot de passe',
            'autocomplete': 'new-password'
        })
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password", "confirm_password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
