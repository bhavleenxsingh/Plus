from django.shortcuts import render, redirect, HttpResponse
from . forms import addf, subf, mulf, quof, remf, expf, primef
# Create your views here.

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
            return HttpResponse("invalid")
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
            return HttpResponse("invalid")
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
            return HttpResponse("invalid")
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
            return HttpResponse("invalid")
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
            return HttpResponse("invalid")
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
            return HttpResponse("invalid")
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
            return HttpResponse("invalid")
    else :
        primei = primef()
        return render(request, "app/prime.html", {"primei": primei})