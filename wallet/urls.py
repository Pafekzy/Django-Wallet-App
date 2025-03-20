from django.urls import path
from .views import wallet_dashboard

urlpatterns = [
    path("dashboard/", wallet_dashboard, name="wallet_dashboard"),
]
