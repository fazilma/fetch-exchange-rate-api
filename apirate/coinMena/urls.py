from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/quotes', views.ExchangeRateView.as_view()),
]