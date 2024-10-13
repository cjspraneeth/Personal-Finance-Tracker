
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.user_login, name='default'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard URL
    path('transactions/add/', views.add_transaction, name='add_transaction'),  # Add transaction URL
    path('transactions/edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),  # Edit transaction URL
    path('transactions/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),  # Delete transaction URL
    path('transactions/', views.list_transactions, name='list_transactions'),  # List transactions URL (if needed separately)
    path('report/monthly/', views.monthly_report, name='monthly_report'),
    path('accounts/', include('allauth.urls')),
    path('budget-goals/', views.budget_goals, name='budget_goals'),
    path('budget-goals/add/', views.add_budget_goal, name='add_budget_goal'),
    path('budget-goals/edit/<int:goal_id>/', views.edit_budget_goal, name='edit_budget_goal'),
    path('budget-goals/delete/<int:goal_id>/', views.delete_budget_goal, name='delete_budget_goal'),

]
