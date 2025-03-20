from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def deposit(self, amount):
        """Add funds to the wallet"""
        if amount > 0:
            self.balance += amount
            self.save()
            return True
        return False

    def withdraw(self, amount):
        """Withdraw funds from the wallet"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.user.username}'s Wallet - Balance: {self.balance}"