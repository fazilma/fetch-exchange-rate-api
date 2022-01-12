from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apirate.coinMena.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
