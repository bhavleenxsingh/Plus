from django.shortcuts import render, redirect, HttpResponse
from . forms import addf, subf, mulf, quof, remf, expf, primef
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def add(request):
    if request.method == 'POST':
        fadd = addf(request.POST)
        if fadd.is_valid():
            fn = fadd.cleaned_data.get('FirstNumber')
            sn = fadd.cleaned_data.get('SecondNumber')
            t = fn + sn
            fadd.save()
            return HttpResponse({t})
        else:
            return HttpResponse("invalid")
    else:
        fadd = addf()
        return render(request, 'app/test.html', {'fadd' : fadd} )
    
def sub(request):
    if request.method == 'POST':
        subi = subf(request.POST)
        if subi.is_valid():
            fn = subi.cleaned_data.get('FirstNumber')
            sn = subi.cleaned_data.get('SecondNumber')
            t = fn - sn
            subi.save()
            return HttpResponse({t})
        else:
            return HttpResponse("invalid")
    else:
        subi = subf()
        return render(request, 'app/test.html', {'subi' : subi} )
    
def mul(request):
    if request.method == 'POST':
        muli = mulf(request.POST)
        if muli.is_valid():
            fn = muli.cleaned_data.get('FirstNumber')
            sn = muli.cleaned_data.get('SecondNumber')
            t = fn * sn
            muli.save()
            return HttpResponse({t})
        else:
            return HttpResponse("invalid")
    else:
        muli = mulf()
        return render(request, 'app/test.html', {'muli' : muli} )
    
def quo(request):
    if request.method == 'POST':
        quoi = quof(request.POST)
        if quoi.is_valid():
            fn = quoi.cleaned_data.get('FirstNumber')
            sn = quoi.cleaned_data.get('SecondNumber')
            t = fn // sn
            quoi.save()
            return HttpResponse({t})
        else:
            return HttpResponse("invalid")
    else:
        quoi = quof()
        return render(request, 'app/test.html', {'quoi' : quoi} )
    
def rem(request):
    if request.method == 'POST':
        remi = remf(request.POST)
        if remi.is_valid():
            fn = remi.cleaned_data.get('FirstNumber')
            sn = remi.cleaned_data.get('SecondNumber')
            t = fn % sn
            remi.save()
            return HttpResponse({t})
        else:
            return HttpResponse("invalid")
    else:
        remi = remf()
        return render(request, 'app/test.html', {'remi' : remi} )
    
def exp(request):
    if request.method == 'POST':
        expi = expf(request.POST)
        if expi.is_valid():
            fn = expi.cleaned_data.get('FirstNumber')
            sn = expi.cleaned_data.get('SecondNumber')
            t = fn ** sn
            expi.save()
            return HttpResponse({t})
        else:
            return HttpResponse("invalid")
    else:
        expi = expf()
        return render(request, 'app/test.html', {'expi' : expi} )

def prime(request):
    list = []
    r = 0
    if request.method == 'POST':
        primei = primef(request.POST)
        if primei.is_valid():
            n = primei.cleaned_data.get('Number')
            for i in range(1, n):
                r = 0
                for j in range(1,i):
                    if i // j == i or 1:
                        r == 1
                        break
                if r == 1:
                    list.append(j)
            return HttpResponse(f"Prime between 0 and {n} are : {list}:")
        else :
            return HttpResponse("invalid")
    else :
        primei = primef()
        return render(request, "app/test.html", {"primei": primei})