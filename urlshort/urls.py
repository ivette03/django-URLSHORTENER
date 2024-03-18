from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_url, name="generate"),
    path('<str:short_url>', views.redirect_url)
    # Add more URL patterns as needed
]
