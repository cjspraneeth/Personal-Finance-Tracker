from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'amount', 'description', 'transaction_type', 'category','receipt']
    # Define predefined categories for expenses
    EXPENSE_CATEGORIES = [
        ('Rent', 'Rent'),
        ('Groceries', 'Groceries'),
        ('Utilities', 'Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Food', 'Food'),
        ('Other', 'Other'),
        # Add more expense categories as needed
    ]
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Enables date picker
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        # Set category field as a CharField for income (string input)
        self.fields['category'].widget = forms.TextInput(attrs={'placeholder': 'Enter category'})

        # Conditionally set category field for expense (dropdown)
        if self.data.get('transaction_type') == 'Expense':
            self.fields['category'] = forms.ChoiceField(choices=self.EXPENSE_CATEGORIES)
    
from django import forms
from .models import BudgetGoal

class BudgetGoalForm(forms.ModelForm):
    class Meta:
        model = BudgetGoal
        fields = ['category', 'goal_amount']    
    