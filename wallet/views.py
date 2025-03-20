from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wallet

@login_required
def wallet_dashboard(request):
    wallet = Wallet.objects.get(user=request.user)
    return render(request, 'wallet/dashboard.html', {'wallet': wallet})
