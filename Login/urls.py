
from django.urls import path
from app_login.views import home, login

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
]
