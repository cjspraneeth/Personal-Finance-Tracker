from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from django.db.models.functions import TruncMonth
from django.db.models import Sum  # Add this line

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Log the user in
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Use the imported login function
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    
    # Calculate total income, expenses, and savings
    total_income = transactions.filter(transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = transactions.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0
    total_savings = total_income - total_expenses  # Calculate savings

    context = {
        'transactions': transactions,
        'data': {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'total_savings': total_savings,
        },
    }

    return render(request, 'dashboard.html', context)

# finance/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm

# View to add a new transaction
@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # Set the user to the currently logged-in user
            transaction.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

# View to edit an existing transaction
@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after editing
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'edit_transaction.html', {'form': form, 'transaction': transaction})

# View to delete a transaction
@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('dashboard')  # Redirect to the dashboard after deletion
    return render(request, 'delete_transaction.html', {'transaction': transaction})

# View to list all transactions
@login_required
def list_transactions(request):
    transactions = Transaction.objects.filter(user=request.user)  # Get transactions for the logged-in user
    return render(request, 'list_transactions.html', {'transactions': transactions})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from django.db.models import functions
from .models import Transaction

@login_required
def monthly_report(request):
    # Get the current user's transactions
    transactions = Transaction.objects.filter(user=request.user)

    # Aggregate income and expenses by month
    monthly_data = (
        transactions
        .annotate(month=functions.TruncMonth('date'))
        .values('month')
        .annotate(total_income=Sum('amount', filter=Q(transaction_type='income')),
                  total_expenses=Sum('amount', filter=Q(transaction_type='expense')))
        .order_by('month')
    )

    context = {
        'monthly_data': monthly_data,
    }
    
    return render(request, 'monthly_report.html', context)