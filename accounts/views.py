from django.shortcuts import render

def login(request):
    return render(request, 'auth/login.html', {'active_page': 'login'})


def register(request):
    return render(request, 'auth/register.html', {'active_page': 'register'})
