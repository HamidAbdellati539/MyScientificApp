from django.urls import path
from . import views

urlpatterns = [
    # Deze lege path ('') betekent dat dit de landingspagina van de app is
    path('', views.health_calculator_view, name='health_calculator'),
]