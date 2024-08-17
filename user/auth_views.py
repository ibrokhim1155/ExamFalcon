from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.forms import AddUserForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('customer_list')
        else:
            messages.error(request, "Invalid registration details.")
            print(form.errors)
    else:
        form = AddUserForm()
    return render(request, 'auth/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.info(request, f"You are now logged in as {email}.")
            return redirect('customer_list')
        else:
            messages.error(request, "Invalid email or password.")

    form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('customer_list')
