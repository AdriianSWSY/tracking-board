from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings

from core.tasks import send_mail_async


class PasswordResetCustomForm(PasswordResetForm):

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        # custom user object in context:
        context['user'] = context['user'].get_username()
        # custom password reset url:
        context['password_reset_url'] = \
            f"{settings.URL_FRONT_RESET_PASSWORD}" \
            f"?uid={context.get('uid')}&token={context.get('token')}"

        # TODO: create reset password email html template
        # custom html tempalte:
        # html_email_template_name = "user/password_reset_body.html"

        # send async mail:
        subject_template_name = 'users/password_reset_subject.txt'
        email_template_name = 'users/password_reset_body.txt'
        send_mail_async.apply_async(kwargs={
            "subject_template_name": subject_template_name,
            "email_template_name": email_template_name,
            # "html_email_template_name": html_email_template_name,
            "context": context,
            "from_email": from_email,
            "to_email": to_email,
            "email_type": "reset password",
        })
