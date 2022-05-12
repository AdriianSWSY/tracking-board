from django.urls import path, include

from apps.users import views as users_views, auth_views

app_name = 'api'
urlpatterns = [

    path('auth/login/',
         users_views.LoginCustomView.as_view(),
         name='rest_login'),

    # default Google and Facebook registration and login
    path('auth/facebook/', auth_views.FacebookLoginView.as_view(),
         name='fb_login_and_signup'),
    path('auth/google/', auth_views.GoogleLoginView.as_view(),
         name='google_login_and_signup'),

    path('auth/', include('dj_rest_auth.urls')),
]
