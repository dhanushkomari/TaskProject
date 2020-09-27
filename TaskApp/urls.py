from django.urls import path
from . import views

app_name = 'TaskApp'

urlpatterns = [
    path('',views.Home.as_view(),name="home"),  
    path('accounts/create/spaccount',views.SignUpSPView,name='sp-create'),
    path('accounts/create/clientaccount',views.SignUpClientView,name='client-create'),
    path('accounts/login-sp',views.loginSPView,name='login-sp'),
    path('accounts/login-client',views.loginClientView,name='login-client'),
    path('accounts/logiin-admin',views.LoginAdminView,name='login-admin'),
    path('accounts/logout/',views.SignOutView,name='signout'),
    
]
