from django.urls import path
from .views import AccountsappSignUpView

urlpatterns = [
    path('signup/', AccountsappSignUpView.as_view(), name='accountsappsignup'),
    ]