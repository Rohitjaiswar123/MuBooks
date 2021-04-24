from django.urls import path
from . import views
urlpatterns = [
path ('', views.home , name ='home'),
path ('home', views.home , name ='home'),
path('SEM1', views.SEM1, name='SEM1'),
path('SEM2', views.SEM2, name='SEM2'),
path('ITSBooks', views.ITSBooks, name='ITSBooks'),
path('MecSBooks', views.MecSBooks, name='MecSBooks'),
path('CompsSBooks', views.CompsSBooks, name='CompsSBooks'),
path('EXTCSBooks', views.EXTCSBooks,name='EXTCSBooks'),
path('ITTBooks', views.ITTBooks, name='ITTBooks'),
path('MecTBooks', views.MecTBooks, name='MecTBooks'),
path('CompsTBooks', views.CompsTBooks, name='CompsTBooks'),
path('EXTCTBooks', views.EXTCTBooks,name='EXTCTBooks'),
path('ITFBooks', views.ITFBooks, name='ITFBooks'),
path('MecFBooks', views.MecFBooks, name='MecFBooks'),
path('CompsFBooks', views.CompsFBooks, name='CompsFBooks'),
path('EXTCFBooks', views.EXTCFBooks,name='EXTCFBooks'),
path('aboutus', views.AboutUs, name='aboutus'),


]

