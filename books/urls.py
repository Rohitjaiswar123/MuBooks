from django.urls import path
from . import views
urlpatterns = [
path ('', views.home , name ='home'),
path ('home', views.home , name ='home'),
path('SEM1', views.SEM1, name='SEM1'),
path('SEM2', views.SEM2, name='SEM2'),
path('ITSBooks', views.ITSBooks, name='ITSBooks'),
path('MecSBooks', views.MecSBooks, name='MecSBooks'),
path('CivilSBooks', views.CivilSBooks, name='CivilSBooks'),
path('ElectricalSBooks', views.ElectricalSBooks,name='ElectricalSBooks'),
path('ITTBooks', views.ITTBooks, name='ITTBooks'),
path('MecTBooks', views.MecTBooks, name='MecTBooks'),
path('CivilTBooks', views.CivilTBooks, name='CivilTBooks'),
path('ElectricalTBooks', views.ElectricalTBooks,name='ElectricalTBooks'),
path('ITFBooks', views.ITFBooks, name='ITFBooks'),
path('MecFBooks', views.MecFBooks, name='MecFBooks'),
path('CivilFBooks', views.CivilFBooks, name='CivilFBooks'),
path('ElectricalFBooks', views.ElectricalFBooks,name='ElectricalFBooks'),
path('aboutus', views.AboutUs, name='aboutus'),


]

