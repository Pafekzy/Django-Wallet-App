from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def deposit(self, amount):
        """Add funds to the wallet and record transaction"""
        if amount > 0:
            self.balance += amount
            self.save()
            Transaction.objects.create(wallet=self, transaction_type="Deposit", amount=amount)
            return True
        return False

    def withdraw(self, amount):
        """Withdraw funds from the wallet and record transaction"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save()
            Transaction.objects.create(wallet=self, transaction_type="Withdraw", amount=amount)
            return True
        return False

    def __str__(self):
        return f"{self.user.username}'s Wallet - Balance: {self.balance}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Deposit', 'Deposit'),
        ('Withdraw', 'Withdraw'),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    from django.db import models
    from django.contrib.auth.models import User

    class Wallet(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
        created_at = models.DateTimeField(auto_now_add=True)

        def deposit(self, amount):
            """Add funds to the wallet and record transaction"""
            if amount > 0:
                self.balance += amount
                self.save()
                Transaction.objects.create(wallet=self, transaction_type="Deposit", amount=amount)
                return True
            return False

        def withdraw(self, amount):
            """Withdraw funds from the wallet and record transaction"""
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.save()
                Transaction.objects.create(wallet=self, transaction_type="Withdraw", amount=amount)
                return True
            return False

        def __str__(self):
            return f"{self.user.username}'s Wallet - Balance: {self.balance}"

    class Transaction(models.Model):
        TRANSACTION_TYPES = [
            ('Deposit', 'Deposit'),
            ('Withdraw', 'Withdraw'),
        ]

        wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")
        transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.transaction_type} of ${self.amount} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    def __str__(self):
        return f"{self.transaction_type} of ${self.amount} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
