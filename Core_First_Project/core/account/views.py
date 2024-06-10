from django.shortcuts import render, HttpResponse ,redirect
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from crudApp.models import userDetail

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        name=request.POST.get("name")
        LastName=request.POST.get("LastName")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm-password")
        user=User.objects.filter(username=username).exists()
        if (user):
            messages.add_message(request,messages.INFO,"User already Exist")
            return render(request, "signup.html")
        
        if password != confirm_password:
            messages.add_message(request,messages.INFO,"password and comfirm password not same")
            return render(request, "signup.html")
        user = User.objects.create(username=username,first_name=name,last_name=LastName)
        user.set_password(password)
        user.save()
        return redirect('/login')

    return render(request, "signup.html")


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User.objects.filter(username=username).exists()
        if (user):
            user =authenticate(request,username=username,password=password)
            if user is None:
                messages.add_message(request,messages.ERROR,"Wrong Password")
                return render(request,'login.html')
            else:
                login(request,user)
                print(request.user.get_full_name())
                return redirect("main_page")
        else:
            messages.add_message(request,messages.INFO,"User Not exist")
            return render(request,'login.html')
            
            
    return render(request,'login.html')

@login_required(login_url='loginuser')
def main_page(request):
    if request.method == "POST":
        name = request.POST.get("search")
        userdetail= userDetail.objects.filter(name__icontains=name)
    else:
        userdetail=userDetail.objects.all()
    context={"userdetail":userdetail}
    return render(request,"index.html",context)

def logoutuser(request):
    logout(request)
    return redirect('main_page')