from django.shortcuts import render, redirect


def home(request):
	return render(request, 'authentication/home.html', {})

def login_user(request):
	return render(request, 'authentication/login.html', {})

def logout_user(request):
	return redirect('home')

def register_user(request):
	return render(request, 'authentication/register.html')

def edit_profile(request):
	return render(request, 'authentication/edit_profile.html')

def change_password(request):
	return render(request, 'authentication/change_password.html')


# path('', views.home, name="home"),
# path('login/', views.login_user, name='login'),
# path('logout/', views.logout_user, name='logout'),
# path('register/', views.register_user, name='register'),
# path('edit_profile/', views.edit_profile, name='edit_profile'),
# path('change_password', views.change_password, name='change_password'),