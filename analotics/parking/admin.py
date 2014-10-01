from django.contrib import admin
from parking.models import Lots, License, CheckIn

# Register your models here.
admin.site.register(Lots)
admin.site.register(License)
admin.site.register(CheckIn)
