from django.urls import path
from .views import wallet_dashboard, home

urlpatterns = [
    path("", home, name="home"),  # ✅ Homepage
    path("dashboard/", wallet_dashboard, name="wallet_dashboard"),
]
