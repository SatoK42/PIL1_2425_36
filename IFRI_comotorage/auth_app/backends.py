from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from phonenumbers import parse as pn_parse, is_valid_number
User = get_user_model()

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        lookup = username.strip()
        user = None
        # Essayer email
        try:
            user = User.objects.get(email__iexact=lookup)
        except User.DoesNotExist:
            # Essayer téléphone : on normalise un peu
            try:
                # on force une région par défaut, ex. 'BJ'
                pn = pn_parse(lookup, 'BJ')
                if is_valid_number(pn):
                    user = User.objects.get(phone_number=pn)
            except Exception:
                user = None
        # Si on a un user et que le mot de passe matche, on renvoie
        if user and user.check_password(password):
            return user
        return None
