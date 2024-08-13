# from django.urls import path
# from django import urls

# from .views import *
# app_name="account"
# urlpatterns = [
#     # path("login/",LoginView.as_view(),name="account-login-register")
# ]

from django.urls import path, reverse_lazy
from .views import *
from  . import views
from django.contrib.auth import views as auth_views
app_name="account_app" 

urlpatterns = [
    path('checkauth/', CheckAuthView.as_view(), name='checkauth'),
    path('register/',views.register_view ,name='register'),
    
    #activate account url
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('login/', views.login_view,name='login'),
    path('logout/', logout_view, name='logout'),

  #pass word reset urls
    path('password-reset/', password_reset_request, name='password_reset'),

    path('password-reset-sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         password_reset_confirm,
         name='password_reset_confirm'),
         
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

]



