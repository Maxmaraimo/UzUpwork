from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('registration_s/', registration_s, name='registration_s'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profile, name='profile')
]