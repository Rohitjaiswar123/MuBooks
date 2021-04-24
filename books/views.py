from django.shortcuts import render
from .models import *

def home (requests):
    return render(requests, 'home.html')
    
def AboutUs (requests):
    return render(requests, 'AboutUs.html')

def SEM1 (requests):
    bookobj1= Sem1.objects.all()    
    return render(requests, 'SEM1.html',{'bookobj1' : bookobj1})
    
def SEM2 (requests):
    bookobj2=Sem2.objects.all()   
    return render(requests, 'SEM2.html',{'bookobj2' : bookobj2})

def ITSBooks (requests):
    bookobj3=ITSEBooks.objects.all() 
    return render(requests, 'ITSBooks.html',{'bookobj3' : bookobj3})
    
def MecSBooks (requests):
    bookobj4=MecSEBooks.objects.all()        
    return render(requests, 'MecSBooks.html',{'bookobj4' : bookobj4})
    
def CompsSBooks (requests):
    bookobj5=CompsSEBooks.objects.all()
    return render(requests, 'CompsSBooks.html',{'bookobj5' : bookobj5})

def EXTCSBooks (requests):
    bookobj6=EXTCSEBooks.objects.all
    return render(requests, 'EXTCSBooks.html',{'bookobj6' : bookobj6})

def ITTBooks (requests):
    bookobj7=ITFEBooks.objects.all()
    return render(requests, 'ITTBooks.html',{'bookobj7' : bookobj7})
    
def MecTBooks (requests):
    bookobj8=MecTEBooks.objects.all()
    return render(requests, 'MecTBooks.html',{'bookobj8' : bookobj8})
    
def CompsTBooks (requests):
    bookobj9=CompsTEBooks.objects.all()
    return render(requests, 'CompsTBooks.html',{'bookobj9' : bookobj9})

def EXTCTBooks (requests):
    bookobj10=EXTCTEBooks.objects.all()
    return render(requests, 'EXTCTBooks.html',{'bookobj10' : bookobj10})

def ITFBooks (requests):
    bookobj11=ITFEBooks.objects.all()
    return render(requests, 'ITFBooks.html',{'bookobj11' : bookobj11})
    
def MecFBooks (requests):
    bookobj12=MecFEBooks.objects.all()
    return render(requests, 'MecFBooks.html',{'bookobj12' : bookobj12})
    
def CompsFBooks (requests):
    bookobj13=CompsFEBooks.objects.all()
    return render(requests, 'CompsFBooks.html',{'bookobj13' : bookobj13})

def EXTCFBooks (requests):
    bookobj14=EXTCFEBooks.objects.all()
    return render(requests, 'EXTCFBooks.html',{'bookobj14' : bookobj14})
    


    

    