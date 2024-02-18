from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import  Employee, Department, Position, User


# Create your views here.
@login_required(login_url='login')
def index(request):
    employees =  Employee.objects.all()
    return render(request, "index.html",{'employees' : employees})      

@login_required(login_url='login')
def create(request):
    if request.method =="GET":
        departments = Department.objects.all()
        positions = Position.objects.all()
        users = User.objects.all()
        managers = []
        for user in users:
            managers.append(user.username)
        return render(request, "create.html", {
            'positions': positions,
            'departments': departments,
            'managers': managers
        })
    
    else:
        department = Department.objects.get(departmentName=request.POST['department'])
        position = Position.objects.get(positions=request.POST['position'])
        manager = User.objects.get(username=request.POST['manager'])
        newEmployee = Employee(
            firstName = request.POST['firstName'],
            lastName = request.POST['lastName'],
            position = position,
            department = department,
            #department = request.POST['department'],
            joiningDate = request.POST['joiningDate'],
            ctc = request.POST['ctc'],
            manager = manager,
        )
        newEmployee.save()
        return HttpResponseRedirect(reverse(index))
    
@login_required(login_url='login')
def edit(request):
    if request.method == "GET":
        employeeID = request.GET["id"]
        employee = Employee.objects.get(id=employeeID)
        departments = Department.objects.all()
        positions = Position.objects.all()
        users = User.objects.all()
        managers = []
        for user in users:
            managers.append(user.username)
        return render(request, "edit.html", {
                            "employee": employee,
                            "positions": positions,
                            "departments": departments,
                            "managers": managers 
                            })
        
    elif request.method == "POST":
        data = request.POST 
        id = data['id']
        employee = Employee.objects.get(id=id)
        employee.firstName = data['firstName']
        employee.lastName = data['lastName']
        if 'department' in data:
            department = Department.objects.get(departmentName=data['department'] )
            employee.department = department
        if 'position' in data:
            position = Position.objects.get(positions=data['position'])
            employee.position = position
        employee.joiningDate = data['joiningDate']
        employee.ctc = data['ctc']
        if 'manager' in data:
            manager = User.objects.get(username=data['manager'])
            employee.manager = manager
        employee.save()
        return HttpResponseRedirect(reverse(index))

@login_required(login_url='login')
def search(request):
    try:
        searchResult = Employee.objects.get(id=request.GET['id'])
        return render(request, 'search.html', { 'employee': searchResult })
    except:
        return render(request,'search.html', {'message': "No results found!"} )

@login_required(login_url='login')
def delete(request):
    id = request.POST['action']
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect(reverse('index'))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]


        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")