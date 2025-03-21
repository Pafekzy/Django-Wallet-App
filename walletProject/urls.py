from django.contrib import admin
from django.urls import path, include  # <-- Include is needed

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # If using Django auth
    path("", include("core.urls")),  # <-- Add this
]
