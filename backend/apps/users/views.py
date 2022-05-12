from dj_rest_auth.views import LoginView


class LoginCustomView(LoginView):
    authentication_classes = []
