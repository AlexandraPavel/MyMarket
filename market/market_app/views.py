from django.shortcuts import render
from .models import User


def homepage(request):
    print(type(render))

    all_users_qs = User.objects.all()

    return render(request, 'homepage.html', {
        "framework_name": "DJANGO",
        'users': all_users_qs
    })


def contact(request):
    print(type(render))

    all_users_qs = User.objects.all()

    return render(request, 'contact.html', {
        "framework_name": "DJANGO",
        'users': all_users_qs
    })


def cart(request):
    print(type(render))

    all_users_qs = User.objects.all()

    return render(request, 'cart.html', {
        "framework_name": "DJANGO",
        'users': all_users_qs
    })


def products(request):
    print(type(render))

    all_users_qs = User.objects.all()

    return render(request, 'products.html', {
        "framework_name": "DJANGO",
        'users': all_users_qs
    })