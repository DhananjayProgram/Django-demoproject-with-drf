from django.urls import path
from . import views as v

urlpatterns =[
    path('register/',v.register,name="register"),
    path('login/',v.loginuser,name="loginuser"),
    path('logoutuser/',v.logoutuser,name="logoutuser"),
    path('mainpage/',v.main_page,name="main_page")
]