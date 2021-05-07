from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', LoginForm.as_view(), name='login'),
    path('logout', login_required(LogoutUser), name='logout')
]
