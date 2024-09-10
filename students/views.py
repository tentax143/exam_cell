from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student, Request
def home(request):
    return render(request, 'students/home.html')
def student_login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        regno = request.POST.get('regno')
        student = Student.objects.create(name=name, regno=regno)
        student.save()
        return redirect('idcard_payment')
    return render(request, 'students/student_login.html')
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Student

def student_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        department = request.POST.get('department')
        
        # Save the student with hashed password
        student = Student.objects.create(
            name=name, 
            roll_number=roll_number, 
            password=make_password(password),  # Hash the password before saving
            department=department
        )
        student.save()
        return redirect('student_login')  # Redirect to login after successful signup

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
def controller_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        controller = Student.objects.create(name=username,regno=password)
        controller.save()
        return redirect('view_requests')
    return render(request, 'students/controller_login.html')
def controller_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        controller = Student.objects.create(name=username,regno=password)
        controller.save()# Save new controller (you should hash the password in a real-world scenario)
        return redirect('view_requests')
    return render(request, 'students/controller_signup.html')
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