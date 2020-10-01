from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreateForm

from django.shortcuts import redirect
# Create your views here.

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('myapp:home')
    if request.method == "POST":

        forms = UserCreateForm(data=request.POST)

        if forms.is_valid():

            user = forms.save()
            user.set_password(user.password)
            user.save()

            return redirect('accounts:login')
        else:
            pass
    else:
        forms = UserCreateForm()
    return render(request,"accounts/signup.html",{"form": forms})