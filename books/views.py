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
    
def CivilSBooks (requests):
    bookobj5=CivilSEBooks.objects.all()
    return render(requests, 'CivilSBooks.html',{'bookobj5' : bookobj5})

def ElectricalSBooks (requests):
    bookobj6=ElectricalSEBooks.objects.all
    return render(requests, 'ElectricalSBooks.html',{'bookobj6' : bookobj6})

def ITTBooks (requests):
    bookobj7=ITFEBooks.objects.all()
    return render(requests, 'ITTBooks.html',{'bookobj7' : bookobj7})
    
def MecTBooks (requests):
    bookobj8=MecTEBooks.objects.all()
    return render(requests, 'MecTBooks.html',{'bookobj8' : bookobj8})
    
def CivilTBooks (requests):
    bookobj9=CivilTEBooks.objects.all()
    return render(requests, 'CivilTBooks.html',{'bookobj9' : bookobj9})

def ElectricalTBooks (requests):
    bookobj10=ElectricalTEBooks.objects.all()
    return render(requests, 'ElectricalTBooks.html',{'bookobj10' : bookobj10})

def ITFBooks (requests):
    bookobj11=ITFEBooks.objects.all()
    return render(requests, 'ITFBooks.html',{'bookobj11' : bookobj11})
    
def MecFBooks (requests):
    bookobj12=MecFEBooks.objects.all()
    return render(requests, 'MecFBooks.html',{'bookobj12' : bookobj12})
    
def CivilFBooks (requests):
    bookobj13=CivilFEBooks.objects.all()
    return render(requests, 'CivilFBooks.html',{'bookobj13' : bookobj13})

def ElectricalFBooks (requests):
    bookobj14=ElectricalFEBooks.objects.all()
    return render(requests, 'ElectricalFBooks.html',{'bookobj14' : bookobj14})
    


    

    