from django.urls import path, include

from apps.users import views as users_views


app_name = 'api'
urlpatterns = [

    path('auth/login/',
         users_views.LoginCustomView.as_view(),
         name='rest_login'),

    path('auth/', include('rest_auth.urls')),
]
