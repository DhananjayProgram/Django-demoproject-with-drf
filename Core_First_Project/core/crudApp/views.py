from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import userDetail
from django.contrib import messages
# Create your views here.


def updateuser(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        age = request.POST.get("Age")
        userdetail = userDetail.objects.create(name=name, age=age)
        userdetail.save()
        messages.add_message(request, messages.INFO,
                             "Record added Succesfully")
        return redirect('main_page')

    return redirect('main_page')


def deleteuser(request, id):
    user = get_object_or_404(userDetail, id=id)
    if (user):
        user.delete()
        messages.add_message(request, messages.INFO,
                             "Record Deleted Succesfully")
        return redirect('main_page')
    messages.add_message(request, messages.INFO,
                         "Record Not Found Succesfully")
    return redirect('main_page')


def edituser(request, id):
    user = get_object_or_404(userDetail, id=id)
    if request.method == "POST":
        name = request.POST.get("Name")
        age = request.POST.get("Age")
        user.name = name
        user.age = age
        user.save()
        messages.add_message(request, messages.INFO,
                             "Record Updated Succesfully")
        return redirect('main_page')

    if (user):
        context = {"user": user}
        return render(request, "update.html", context)
def searchUser(request):
    pass
    # if request.method == "POST":
    #     name = request.POST.get("search")
    #     data=
