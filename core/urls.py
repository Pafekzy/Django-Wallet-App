from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),  # Root URL
    path("signup/", signup, name="signup"),
]