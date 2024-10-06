from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    date = models.DateField()  # Transaction date
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    description = models.TextField()  # Description of the transaction
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)  # Income or Expense
    category = models.CharField(max_length=100)  # User-defined category as a string
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.amount} on {self.date} ({self.category})"
