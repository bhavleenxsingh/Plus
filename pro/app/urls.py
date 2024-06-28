from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add', views.add, name = 'add'),
    path('sub', views.sub, name = 'sub'),
    path('mul', views.mul, name = 'mul'),
    path('quo', views.quo, name = 'quo'),
    path('rem', views.rem, name = 'rem'),
    path('exp', views.exp, name = 'exp'),
    path('prime', views.prime, name = 'prime'),
    path('otp', views.otp, name = 'otp'),
    path('fib', views.fib, name = 'fib'),
    path('sqrt', views.sqrt, name = 'sqrt'),
    path('cbrt', views.cbrt, name = 'cbrt'),
    path('fac', views.fac, name = 'fac'),
]
