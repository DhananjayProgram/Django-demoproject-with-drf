import json
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests


# Create your views here.

def register(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        team = request.POST['teamdropdown']
        password =request.POST['password']
        confirmpassword =request.POST['confirmpassword']
        if password != confirmpassword :
            messages.add_message(request, messages.WARNING, "Password and Confirm Password does not match")
            return redirect('register')
        if CustomUser.objects.filter(email = email).exists():
            messages.add_message(request, messages.INFO, "User Already Exist")
            return redirect("login")
            
        user = CustomUser(first_name=firstname, last_name=lastname, email=email, team_name=team)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "User Account Created")
        return redirect('register')
    return render(request , "register.html")

def loginUser(request):
    if request.user.is_authenticated :    
        return redirect ('task')
    if request.method == "POST":
        email=request.POST['email']
        password =request.POST['password']
        if not CustomUser.objects.filter(email = email).exists() :
            messages.add_message(request, messages.WARNING, "User Not Exist")
            return redirect('login')
        user = authenticate(email=email,password=password)
        if user is None :
            messages.error(request , "Invalid Password !")
            return redirect('login')
        else :
            login(request , user)
            return redirect ('task')
        
    else:    
        return render(request , "login.html")
    
@login_required()
def UserTask(request):

    url = "http://127.0.0.1:8000/list"

    payload = {}


    response = requests.request("GET", url, data=payload)
    context =  json.loads(response.text)
    print(context)
    




    return render(request , "task.html"  ,{"data":context})


def logoutuser(request):
    if request.user.is_authenticated :  
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
    

