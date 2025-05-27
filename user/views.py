from django.shortcuts import render

# Create your views here.

def sign_up(request):
    ctx = {

    }
    return render(request,'user/register.html',ctx)

def sign_in(request):
    ctx = {

    }
    return render(request,'user/logen.html',ctx)

def sign_out(request):
    pass