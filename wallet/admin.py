from django.contrib import admin
from .models import Wallet, Transaction  # Import models only once

# Register models correctly
admin.site.register(Wallet)
admin.site.register(Transaction)
