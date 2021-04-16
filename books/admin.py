from django.contrib import admin
from django.apps import apps
#from .models import Sem1Books,Sem2Books,ITSBooks,MecSBooks,CivilSBooks,ElectricalSBooks,ITTBooks,MecTBooks,CivilTBooks,ElectricalTBooks,ITFBooks,MecFBooks,CivilFBooks,ElectricalFBooks

# Register your models here.



models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# Register your models here.
