from django.urls import path, include


app_name = 'api'
urlpatterns = [

    path('auth/', include('rest_auth.urls')),
]
