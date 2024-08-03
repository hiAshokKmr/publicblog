# from django.urls import path
# from django import urls

# from .views import *
# app_name="account"
# urlpatterns = [
#     # path("login/",LoginView.as_view(),name="account-login-register")
# ]

from django.urls import path
from .views import *
from  . import views
app_name="account_app" 

urlpatterns = [
    path('checkauth/', CheckAuthView.as_view(), name='checkauth'),
    path('register/',views.register_view ,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', logout_view, name='logout'),
    # Add other URLs as needed
]
