from django.shortcuts import render, redirect, HttpResponse
from . forms import addf, subf, mulf, quof, remf, expf, primef, otpf, fibf, sqrtf, cbrtf, facf
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
    try :
        if request.method == 'POST':
            quoi = quof(request.POST)
            if quoi.is_valid():
                fn = quoi.cleaned_data.get('FirstNumber')
                sn = quoi.cleaned_data.get('SecondNumber')
                t = fn / sn
                quoi.save()
                return render(request, "app/result.html", {'t':t})
            else:
                return render(request, "app/invalid.html")
        else:
            quoi = quof()
            return render(request, 'app/quo.html', {'quoi' : quoi} )
    except :
        return render(request, 'app/zde.html')
    
def rem(request):
    try :
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
    except :
        return render(request, 'app/zde.html')
    
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
            if n > 0 :
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
                return render(request, 'app/noneg.html')
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
            if n > 0 :
                for i in range(n):
                    t = t + num[math.floor(random.random() * 10)]
                return render(request, "app/result.html", {'t': t.strip()})
            else :
                return render(request, 'app/noneg.html')
        else :
            return render(request, "app/invalid.html")
    else :
        otpi = otpf()
        return render(request, "app/otp.html", {'otpi': otpi})

def fib(request):
    try :
        if request.method == 'POST':
            fibi = fibf(request.POST)
            if fibi.is_valid():
                fibi.save()
                n = fibi.cleaned_data.get('Number')
                a = 0
                b = 1
                t = []
                if n > 0:
                    while a < n:
                        t.append(a)
                        a, b = b, a + b
                    return render(request, 'app/result.html', {'t': t})
                else :
                    return render(request, 'app/noneg.html')
            else :
                return render(request, 'app/invalid.html')
        else :
            fibi = fibf()
            return render(request, "app/fib.html", {'fibi': fibi})
    except :
        return render(request, 'app/noneg.html')
        
def sqrt(request):
    if request.method == 'POST':
        sqrti = sqrtf(request.POST)
        if sqrti.is_valid():
            sqrti.save()
            n = sqrti.cleaned_data.get('Number')
            if n > 0 :
                t = n ** (1/2)
                return render(request, 'app/result.html', {'t': t})
            else :
                return render(request, 'app/noneg.html')
        else :
            return render(request, 'app/invalid.html')
    else :
        sqrti = sqrtf()
        return render(request, "app/sqrt.html", {'sqrti': sqrti})
    
def cbrt(request):
    if request.method == 'POST':
        cbrti = cbrtf(request.POST)
        if cbrti.is_valid():
            cbrti.save()
            n = cbrti.cleaned_data.get('Number')
            if n > 0 :
                t = n ** (1/3)
                return render(request, 'app/result.html', {'t': t})
            else :
                return render(request, 'app/noneg.html')
        else :
            return render(request, 'app/invalid.html')
    else :
        cbrti = cbrtf()
        return render(request, "app/cbrt.html", {'cbrti': cbrti})
    
def fac(request) :
    try :
        if request.method == 'POST':
            faci = facf(request.POST)
            if faci.is_valid() :
                faci.save()
                n = faci.cleaned_data.get('Number')
                def fcr(x):
                    if x == 0 or x == 1:
                        return 1
                    else :
                        x = x * fcr(x-1)
                        return x
                t = fcr(n)
                return render(request, 'app/result.html', {'t': t})
            else :
                return render(request, 'app/invalid.html')
        else :
            faci = facf()
            return render(request, 'app/fac.html', {'faci': faci})
    except :
        return render(request, 'app/noneg.html')