from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserLogoutView,UserBankAccountUpdateView
from . import views


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
    path('password_change/', views.password_change, name='password_change'),
]