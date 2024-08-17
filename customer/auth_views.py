# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from customer.forms import AuthenticationForm, AddUserForm
#
# def register(request):
#     if request.method == 'POST':
#         form = AddUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             login(request, user)
#             messages.success(request, f"Account created for!")
#             return redirect('customer_list')
#         messages.error(request, "Invalid username or password")
#
#     form = AddUserForm()
#     return render(request, 'auth/register.html', {'form': form})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             messages.info(request, f"You are now logged in as {username}.")
#             return redirect('customer_list')
#         else:
#             messages.error(request, "Invalid username or password.")
#
#     return render(request, 'auth/login.html')
#
#
# def user_logout(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.")
#     return redirect('customer_list')
#
