from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student_login/', views.student_login, name='student_login'),
    path('idcard_payment/', views.idcard_payment, name='idcard_payment'),
    path('both_payment/', views.both_payment, name='both_payment'),
    path('duplicate_request/', views.duplicate_request, name='duplicate_request'),
    path('controller_login/', views.controller_login, name='controller_login'),
    path('controller_signup/', views.controller_signup, name='controller_signup'),
    path('view_requests/', views.view_requests, name='view_requests'),
    path('hallticket_payment/', views.hallticket_payment, name='hallticket_payment'),
    path('payment_successful/', views.payment_successful, name='payment_successful'),
    path('hallticket_template/', views.hallticket_template, name='hallticket_template'),
    path('idcard_template/', views.idcard_template, name='idcard_template'),
    path('both_template/', views.both_template, name='both_template'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('signup/', views.student_signup, name='student_signup'),
]