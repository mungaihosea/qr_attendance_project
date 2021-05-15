from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user

def login(request):
    error = None
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        try:
            user = User.objects.get(username = username)
            if user.check_password(password):
                login_user(request, user)
                return redirect('dash')
            else:
                error = "Invalid login credentials"
        except Exception as e:
            error = "Invalid login credentials"
            print(e)
    return render(request, 'login.html', {"error":error})


def dashboard(request):
    #create a user which will also create a qr for them
    #create a url to mark attendance
    
    return render(request, 'dash.html', {})