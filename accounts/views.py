from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid User or Password")
                return redirect("login")

    context = {
        "forms": forms
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}.Please Login!')
            return redirect('login')
    else: 
        form=UserCreationForm()
    return render(request,'accounts/register.html',{'form':form})
