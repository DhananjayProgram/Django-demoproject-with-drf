from django.urls import path
from . import views as v

urlpatterns=[
    path('update/',v.updateuser,name="update"),
    path('delete/<int:id>/',v.deleteuser,name="delete"),
    path('edit/<int:id>/',v.edituser,name="edit"),
    path("searchUser",v.searchUser,name='searchUser')
]