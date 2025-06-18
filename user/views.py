from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect

from user.models import User


# Create your views here.



def sign_up(request):
    ctx = {}
    if request.POST:
        data=request.POST

        username = data.get('username',None)
        email = data.get ('email', None)
        password = data.get('password', None)
        phone = data.get('phone', None)

        if None in [username,email,password,phone]:
            ctx['error'] = "qatorni to'ldiring!!!"
            return render(request, 'user/register.html', ctx)

        user = User.objects.filter(username=username).first()
        if user:
            ctx['error'] = 'bunaqa user yaratilgan'
            return render(request, 'user/register.html', ctx)

        user = User.objects.create_user(username=username, email=email, password=password, phone=phone)
        login(request, user)
        authenticate(request)
        return redirect('home')

    return render(request,'user/register.html',ctx)

def sign_in(request):
    ctx = {}

    if request.POST:
        data = request.POST
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email,password]:
            ctx['error'] = 'qatorni tuldiring!!!'
            return render(request, 'user/login.html', ctx)

        user = User.objects.filter(email=email).first()

        if user is None:
            ctx['error'] = 'Bunaqa user mavjut emas'
            return render(request, 'user/login.html', ctx)


        logout(request)
        return redirect('home')

    return render(request,'user/login.html',ctx)

def sign_out(request):
        logout(request)
        return redirect('register')