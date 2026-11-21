
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Product

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# USER REGISTRATION
def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'students/register.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'students/register.html', {
                'error': 'Username already exists'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'students/register.html', {
                'error': 'Email already exists'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'students/register.html')


# STUDENT FORM
def student_form(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )


# STUDENT LIST
def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )


# USER LOGIN
def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            return render(request, "students/login.html", {
                'error': "Invalid Username or password"
            })

    return render(request, 'students/login.html')


# DASHBOARD
@login_required(login_url='login')
def dashboard(request):

    return render(request, 'students/dashboard.html')


# USER LOGOUT
def logout_page(request):

    if request.method == "POST":
        logout(request)

    return redirect('login')


# HOME PAGE
def home(request):

    return render(request, 'students/home.html')


# PRODUCT LIST
def products(request):

    all_products = Product.objects.all()

    return render(
        request,
        'students/products.html',
        {
            'products': all_products
        }
    )
