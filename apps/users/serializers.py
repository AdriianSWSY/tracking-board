from rest_auth.serializers import PasswordResetSerializer

from .forms import PasswordResetCustomForm


class PasswordResetCustomSerializer(PasswordResetSerializer):
    password_reset_form_class = PasswordResetCustomForm
