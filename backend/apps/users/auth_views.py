import requests
from allauth.socialaccount import providers
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.providers.facebook.provider import \
    FacebookProvider, GRAPH_API_URL
from allauth.socialaccount.providers.facebook.views import \
    FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from drf_yasg.utils import swagger_auto_schema as swagger
from rest_auth.registration.views import SocialLoginView

from apps.core.swagger_utils import social_auth_schema, AuthResponseSerializer


def check_social_sign_up(extra_data, request):
    """
    You can do here some validations about user social sign ap.
    If something goes wring here just do next:
        raise serializers.ValidationError('Some error text.')
    """
    pass


class CustomGoogleOAuth2Adapter(GoogleOAuth2Adapter):
    """Overridden for including check_social_sign_up step."""
    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.profile_url,
                            params={'access_token': token.token,
                                    'alt': 'json'})
        resp.raise_for_status()
        extra_data = resp.json()
        check_social_sign_up(extra_data, request)
        login = self.get_provider() \
            .sociallogin_from_response(request,
                                       extra_data)
        return login


class CustomFacebookOAuth2Adapter(FacebookOAuth2Adapter):
    """
    Overridden for including check_social_sign_up step.
    Also in default Facebook OAuth2Adapter there is 'appsecret_proof' parameter
    in request to Facebook, and here it is not. 'appsecret_proof' needs
    for  more security. By default in Facebook Developer app this parameter
    is disabled, so, if you want, you can enable it and add into
    request in complete_login() method like this:
        'appsecret_proof': compute_appsecret_proof(app, token).
    """
    def complete_login(self, request, app, access_token, **kwargs):
        provider = providers.registry.by_id(FacebookProvider.id, request)
        resp = requests.get(
            GRAPH_API_URL + '/me',
            params={
                'fields': ','.join(provider.get_fields()),
                'access_token': access_token.token
            })
        resp.raise_for_status()
        extra_data = resp.json()
        check_social_sign_up(extra_data, request)
        login = provider.sociallogin_from_response(request, extra_data)
        return login


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Here you can do some social registration staff with user model
    like add extra data.
    """

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        return user


class FacebookLoginView(SocialLoginView):
    authentication_classes = ()
    adapter_class = CustomFacebookOAuth2Adapter

    @swagger(request_body=social_auth_schema,
             responses={200: AuthResponseSerializer, 400: 'Incorrect value'})
    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)


class GoogleLoginView(SocialLoginView):
    authentication_classes = ()
    adapter_class = CustomGoogleOAuth2Adapter

    @swagger(request_body=social_auth_schema,
             responses={200: AuthResponseSerializer, 400: 'Incorrect value'})
    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)
