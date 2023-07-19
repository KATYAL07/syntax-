from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        mobile = request.POST['mobile']
        email = request.POST['email']

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.first_name = name
        user.save()

        # Redirect to a success page or perform any other actions
        # return render(request, 'signin.html')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'signin.html', {'error_message': error_message})
    # else:
    return render(request, 'signin.html')


def welcome_view(request):
    return render(request, 'welcome.html')


def choose_locker_view(request):
    return render(request, 'choose_locker.html')
