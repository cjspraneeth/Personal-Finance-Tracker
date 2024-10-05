
from django.urls import path
from .views import register, user_login, logout_view, dashboard, add_transaction, edit_transaction, delete_transaction, list_transactions

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard URL
    path('transactions/add/', add_transaction, name='add_transaction'),  # Add transaction URL
    path('transactions/edit/<int:transaction_id>/', edit_transaction, name='edit_transaction'),  # Edit transaction URL
    path('transactions/delete/<int:transaction_id>/', delete_transaction, name='delete_transaction'),  # Delete transaction URL
    path('transactions/', list_transactions, name='list_transactions'),  # List transactions URL (if needed separately)
]
