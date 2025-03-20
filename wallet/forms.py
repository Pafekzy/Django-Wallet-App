from django import forms

class TransactionForm(forms.Form):
    TRANSACTION_TYPES = [
        ("Deposit", "Deposit"),
        ("Withdraw", "Withdraw"),
    ]

    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPES, widget=forms.RadioSelect)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)