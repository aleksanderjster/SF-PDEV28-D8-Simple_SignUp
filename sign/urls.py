from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# for signup example
from .views import BaseRegisterView

urlpatterns = [
    path('login/', 
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/', 
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
     # for signup example
     path('signup/', 
         BaseRegisterView.as_view(template_name = 'sign/signup.html'), 
         name='signup'),
]