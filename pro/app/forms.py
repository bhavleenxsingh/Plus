from django import forms
from . models import addm, subm, mulm, quom, remm, expm, primem, otpm, fibm, sqrtm, cbrtm, facm

class addf(forms.ModelForm):
    
    class Meta:
        model = addm
        fields = ['FirstNumber', 'SecondNumber']
        
class subf(forms.ModelForm):
    
    class Meta:
        model = subm
        fields = ['FirstNumber', 'SecondNumber']
        
class mulf(forms.ModelForm):
    
    class Meta:
        model = mulm
        fields = ['FirstNumber', 'SecondNumber']
        
class quof(forms.ModelForm):
    
    class Meta:
        model = quom
        fields = ['FirstNumber', 'SecondNumber']
        
class remf(forms.ModelForm):
    
    class Meta:
        model = remm
        fields = ['FirstNumber', 'SecondNumber']
        
class expf(forms.ModelForm):
    
    class Meta:
        model = expm
        fields = ['FirstNumber', 'SecondNumber']
        
class primef(forms.ModelForm):
    
    class Meta:
        model = primem
        fields = ['Number']
        
class otpf(forms.ModelForm):
    
    class Meta:
        model = otpm
        fields = ['Number']
        
class fibf(forms.ModelForm):
    
    class Meta:
        model = fibm
        fields = ['Number']
        
class sqrtf(forms.ModelForm):
    
    class Meta:
        model = sqrtm
        fields = ['Number']
        
class cbrtf(forms.ModelForm):
    
    class Meta:
        model = cbrtm
        fields = ['Number']
        
class facf(forms.ModelForm):
    
    class Meta:
        model = facm
        fields = ['Number']
        
