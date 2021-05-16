from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user
import requests
from .models import Admin, Employee, Settings, Record


def login(request):
    error = None
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print('username', username)
        print('password', password)
        try:
            print([x.username for x in Admin.objects.all()])
            user = Admin.objects.get(username = username)
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
    print(request.META['REMOTE_ADDR'])
    success = None
    
    #create a user which will also create a qr for them
    #create a url to mark attendance
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)

        e = Employee()
        e.username = username
        e.email = email
        e.save()
        success = "Employee has been added successfully"
    employees = Employee.objects.all()
    context = {
        'port': Settings.objects.get().port,
        'ip': Settings.objects.get().ip,
        'success':success,
        'employees': employees
    }
    return render(request, 'dash.html', context)


def logout(request):
    logout_user(request)
    return redirect('login')

def set_ip(request):
    success = None
    print(request.POST)
    if request.method == 'POST':
        current_ip = Settings.objects.get()
        current_ip.ip = request.POST.get('ip', None)
        current_ip.port = request.POST.get('port', None)
        current_ip.save()       
    return redirect('dash')

# ipaddress:port/scan_page/uid
def scan_page(request, id):
    user = get_object_or_404(Employee, id = id)
    context = {
        'user':user        
    }
    return render(request, 'scan_page.html', context)

# ipaddress:port/check_in/uid
def check_in(request, id):
    user = get_object_or_404(Employee, id = id)
    record = Record()
    record.user = user
    record.activity = "check in"
    record.save()
    context = {
        'user':user,
        'record_activity': "check in"
    }
    return render(request, 'success.html', context)

def check_out(request, id):
    user = get_object_or_404(Employee, id = id)
    record = Record()
    record.user = user
    record.activity = "check out"
    record.save()

    context = {
        'user':user,
        'record_activity': "check out"
    }
    return render(request, 'success.html', context)