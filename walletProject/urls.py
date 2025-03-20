from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", lambda request: redirect("wallet_dashboard")),  # ✅ Redirect to dashboard
    path("admin/", admin.site.urls),
    path("wallet/", include("wallet.urls")),
]

