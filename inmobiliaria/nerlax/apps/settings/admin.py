from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Company)
admin.site.register(Classification)
admin.site.register(ActivityType)
admin.site.register(Supplier)
admin.site.register(Services)
