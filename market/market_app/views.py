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



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("main:homepage")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})