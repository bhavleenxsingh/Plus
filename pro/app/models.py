from django.db import models
from datetime import datetime
# Create your models here.

class addm(models.Model):
    FirstNumber = models.IntegerField()
    SecondNumber = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.FirstNumber} & {self.SecondNumber} at {self.Time}'
    
class subm(models.Model):
    FirstNumber = models.IntegerField()
    SecondNumber = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.FirstNumber} & {self.SecondNumber} at {self.Time}'
    
class mulm(models.Model):
    FirstNumber = models.IntegerField()
    SecondNumber = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.FirstNumber} & {self.SecondNumber} at {self.Time}'
    
class quom(models.Model):
    FirstNumber = models.IntegerField()
    SecondNumber = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.FirstNumber} & {self.SecondNumber} at {self.Time}'
    
class remm(models.Model):
    FirstNumber = models.IntegerField()
    SecondNumber = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.FirstNumber} & {self.SecondNumber} at {self.Time}'
    
class expm(models.Model):
    FirstNumber = models.IntegerField()
    SecondNumber = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.FirstNumber} & {self.SecondNumber} at {self.Time}'

class primem(models.Model):
    Number = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Number} & {self.Time}'
    
class otpm(models.Model):
    Number = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Number} & {self.Time}'
    
class fibm(models.Model):
    Number = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Number} & {self.Time}'
    
class sqrtm(models.Model):
    Number = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Number} & {self.Time}'
    
class cbrtm(models.Model):
    Number = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Number} & {self.Time}'

class facm(models.Model):
    Number = models.IntegerField()
    Time = models.DateTimeField(default = datetime.now())
    
    def __str__(self):
        return f'{self.Number} & {self.Time}'
