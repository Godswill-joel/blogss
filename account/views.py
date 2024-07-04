from django.shortcuts import render, redirect
from account.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def register(request):
    if request.methid == 'POST':
        form  = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }     
    return render(request, 'account/register.html', context)



def Login(request):
    if request.method == "POST":
       email = request.POST["email"]
       password = request.POST["password"]
       user = authenticate(request, email=email,password=password)
       if user is not None:
        login(request,user)
        redirect("/")
        messages.error(request, "Invalid Email or Password")
    return render(request, "account/login.html")

