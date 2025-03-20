from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wallet, Transaction
from .forms import TransactionForm

@login_required
def wallet_dashboard(request):
    wallet, created = Wallet.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            transaction_type = request.POST.get("transaction_type")

            if transaction_type == "Deposit":
                wallet.deposit(amount)
                messages.success(request, f"Deposited ${amount} successfully!")
            elif transaction_type == "Withdraw":
                if wallet.withdraw(amount):
                    messages.success(request, f"Withdrew ${amount} successfully!")
                else:
                    messages.error(request, "Insufficient funds!")

        return redirect("wallet_dashboard")

    else:
        form = TransactionForm()

    transactions = wallet.transactions.all().order_by("-timestamp")  # Fetch latest transactions

    return render(request, "wallet/dashboard.html", {"wallet": wallet, "form": form, "transactions": transactions})