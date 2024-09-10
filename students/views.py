from django.shortcuts import render, redirect
from .models import Student, Request, Controller
from django.http import HttpResponse

def student_login(request):
    if request.method == "POST":
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(roll_number=roll_number)
        except Student.DoesNotExist:
            return render(request, 'students/student_login.html', {'error': 'Invalid credentials!'})

        if student.check_password(password):
            return redirect('idcard_payment')
        else:
            return render(request, 'students/student_login.html', {'error': 'Invalid credentials!'})

    return render(request, 'students/student_login.html')

def student_signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        department = request.POST.get('department')

        if Student.objects.filter(roll_number=roll_number).exists():
            return render(request, 'students/student_signup.html', {'error': 'Roll number already exists!'})

        student = Student(name=name, roll_number=roll_number, department=department)
        student.set_password(password)
        student.save()

        return redirect('student_login')

    return render(request, 'students/student_signup.html')

def idcard_payment(request):
    if request.method == "POST":
        return redirect('both_payment')
    return render(request, 'students/idcard_payment.html')

def both_payment(request):
    if request.method == "POST":
        return redirect('duplicate_request')
    return render(request, 'students/both_payment.html')

def hallticket_payment(request):
    if request.method == "POST":
        return redirect('duplicate_request')
    return render(request, 'students/hallticket_payment.html')

def hallticket_template(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'students/hallticket_template.html')

def idcard_template(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'students/idcard_template.html')

def both_template(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'students/both_template.html')

def duplicate_request(request):
    if request.method == "POST":
        return HttpResponse('Request was sent')
    return render(request, 'students/duplicate_request.html')

def view_requests(request):
    requests = Request.objects.all()
    return render(request, 'students/view_requests.html', {'requests': requests})

def payment_page(request):
    if request.method == 'POST':
        return redirect('payment_successful')
    return render(request, 'students/payment.html')

def payment_successful(request):
    return render(request, 'students/payment_successful.html')

def contact_us(request):
    return render(request, 'students/contact_us.html')

from django.shortcuts import render, redirect
from .models import Controller
from django.contrib.auth import authenticate, login

def controller_login(request):
    if request.method == "GET":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        print(f"Username: {username}, Role: {role}, Password: {password}")


        # Authenticate user
        try:
            controller = Controller.objects.get(username=username)
            if controller.check_password(password) and controller.role == role:
                # Perform login
                login(request, controller)  # Optional if using Django's auth system
                return redirect('view_requests')  # Redirect to view_requests page
            else:
                return render(request, 'students/controller_login.html', {'error': 'Invalid credentials or role!'})
        except Controller.DoesNotExist:
            return render(request, 'students/controller_login.html', {'error': 'Controller not found!'})

    return render(request, 'students/controller_login.html')


from django.shortcuts import render, redirect
from .models import Controller

def controller_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        print(f"Username: {username}, Email: {email}, Role: {role}, Password: {password}")


        # Check if the controller already exists
        if Controller.objects.filter(username=username).exists():
            return render(request, 'students/controller_signup.html', {'error': 'Username already exists!'})

        # Create a new controller and hash the password
        controller = Controller(username=username, email=email, role=role)
        controller.set_password(password)  # Hash and save password
        controller.save()

        return redirect('controller_login')  # Redirect to login page after successful signup

    return render(request, 'students/controller_signup.html')

from django.shortcuts import render

def home(request):
    return render(request, 'students/home.html')
