from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('register/', UsersRegister.as_view(), name='register'),
    path('logout/', login_required(logoutUser), name='logout'),

    path('list_user/', login_required(ListUsers.as_view()), name='list-users'),
    path('create/', login_required(CreateUsers.as_view()), name='create-users'),
    path('profile/<int:pk>', login_required(UpdateProfileUser.as_view()), name='profile-users'),
]

# url de vista implicitas
urlpatterns += [
    path('users/', login_required(TemplateView.as_view(template_name='users/users.html')), name='users'),
]
