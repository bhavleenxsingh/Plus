from django.shortcuts import render, redirect, HttpResponse
from . forms import addf, subf, mulf, quof, remf, expf, primef, otpf
# Create your views here.
import math, random
def home(request):
    return render(request, 'app/home.html')

def add(request):
    if request.method == 'POST':
        addi = addf(request.POST)
        if addi.is_valid():
            fn = addi.cleaned_data.get('FirstNumber')
            sn = addi.cleaned_data.get('SecondNumber')
            t = fn + sn
            addi.save()
            return render(request, "app/result.html", {'t':t})
        else:
            return render(request, "app/invalid.html")
    else:
        addi = addf()
        return render(request, 'app/add.html', {'addi' : addi} )
    
def sub(request):
    if request.method == 'POST':
        subi = subf(request.POST)
        if subi.is_valid():
            fn = subi.cleaned_data.get('FirstNumber')
            sn = subi.cleaned_data.get('SecondNumber')
            t = fn - sn
            subi.save()
            return render(request, "app/result.html", {'t':t})
        else:
            return render(request, "app/invalid.html")
    else:
        subi = subf()
        return render(request, 'app/sub.html', {'subi' : subi} )
    
def mul(request):
    if request.method == 'POST':
        muli = mulf(request.POST)
        if muli.is_valid():
            fn = muli.cleaned_data.get('FirstNumber')
            sn = muli.cleaned_data.get('SecondNumber')
            t = fn * sn
            muli.save()
            return render(request, "app/result.html", {'t':t})
        else:
            return render(request, "app/invalid.html")
    else:
        muli = mulf()
        return render(request, 'app/mul.html', {'muli' : muli} )
    
def quo(request):
    if request.method == 'POST':
        quoi = quof(request.POST)
        if quoi.is_valid():
            fn = quoi.cleaned_data.get('FirstNumber')
            sn = quoi.cleaned_data.get('SecondNumber')
            t = fn // sn
            quoi.save()
            return render(request, "app/result.html", {'t':t})
        else:
            return render(request, "app/invalid.html")
    else:
        quoi = quof()
        return render(request, 'app/quo.html', {'quoi' : quoi} )
    
def rem(request):
    if request.method == 'POST':
        remi = remf(request.POST)
        if remi.is_valid():
            fn = remi.cleaned_data.get('FirstNumber')
            sn = remi.cleaned_data.get('SecondNumber')
            t = fn % sn
            remi.save()
            return render(request, "app/result.html", {'t':t})
        else:
            return render(request, "app/invalid.html")
    else:
        remi = remf()
        return render(request, 'app/rem.html', {'remi' : remi} )
    
def exp(request):
    if request.method == 'POST':
        expi = expf(request.POST)
        if expi.is_valid():
            fn = expi.cleaned_data.get('FirstNumber')
            sn = expi.cleaned_data.get('SecondNumber')
            t = fn ** sn
            expi.save()
            return render(request, "app/result.html", {'t':t})
        else:
            return render(request, "app/invalid.html")
    else:
        expi = expf()
        return render(request, 'app/exp.html', {'expi' : expi} )

def prime(request):
    t = []
    if request.method == 'POST':
        primei = primef(request.POST)
        if primei.is_valid():
            n = primei.cleaned_data.get('Number')
            for i in range(1, n):
                r = 0
                for j in range(2,i):
                    if i % j == 0:
                        r = 1
                        break
                if r == 0:
                    t.append(i)
                    primei.save()
            return render(request, "app/result.html", {'t':t})
        else :
            return render(request, "app/invalid.html")
    else :
        primei = primef()
        return render(request, "app/prime.html", {"primei": primei})
    
def otp(request):
    if request.method == "POST":
        otpi = otpf(request.POST)
        if otpi.is_valid():
            otpi.save()
            n = otpi.cleaned_data.get('Number')
            num = "0123456789"
            t = " "
            for i in range(n):
                t = t + num[math.floor(random.random() * 10)]
            return render(request, "app/result.html", {'t': t.strip()})
        else :
            return render(request, "app/invalid.html")
    else :
        otpi = otpf()
        return render(request, "app/otp.html", {'otpi': otpi})