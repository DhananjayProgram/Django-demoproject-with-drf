from django.urls import path 
from . import views as v
urlpatterns = [
    path('register',v.register , name="register")   , 
    path('',v.loginUser , name="login"),
    path('task',v.UserTask , name="task"),
    path('logoutuser',v.logoutuser , name="logout")
]
