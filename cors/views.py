from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required(login_url='register')
def index(request):
    ctx={

    }
    return render(request,'site/index.html',ctx)

@login_required(login_url='register')
def account(request):
    ctx={

    }
    return render(request,'site/account.html',ctx)

@login_required(login_url='register')
def cart(request):
    ctx={

    }
    return render(request,'site/cart.html',ctx)

@login_required(login_url='register')
def categories(request):
    ctx={

    }
    return render(request,'site/categories.html',ctx)

@login_required(login_url='register')
def checkout(request):
    ctx={

    }
    return render(request,'site/checkout.html',ctx)

@login_required(login_url='register')
def product_d(request):
    ctx={

    }
    return render(request,'site/product-detail.html',ctx)

@login_required(login_url='register')
def search(request):
    ctx={

    }
    return render(request,'site/search.html',ctx)

@login_required(login_url='register')
def product(request):
    ctx={

    }
    return render(request,'site/products.html',ctx)

