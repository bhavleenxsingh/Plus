from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('Addition', views.add, name = 'add'),
    path('Subtraction', views.sub, name = 'sub'),
    path('Multiplication', views.mul, name = 'mul'),
    path('Quotient', views.quo, name = 'quo'),
    path('Remainder', views.rem, name = 'rem'),
    path('Exponent', views.exp, name = 'exp'),
    path('Prime_Numbers', views.prime, name = 'prime'),
    path('OTP_Generator', views.otp, name = 'otp'),
    path('Fibonacci_Series', views.fib, name = 'fib'),
    path('Square_Root', views.sqrt, name = 'sqrt'),
    path('Cube_Root', views.cbrt, name = 'cbrt'),
    path('Factorial', views.fac, name = 'fac'),
    path('Miles', views.mile, name = 'mile'),
    path('Inches', views.inch, name = 'inch'),
]
