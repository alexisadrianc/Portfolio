from django.contrib import admin


from .models import *

admin.site.register(Amenities)
admin.site.register(Building)
admin.site.register(Unit)
admin.site.register(CommonExpenses)
admin.site.register(CommonExpensesLines)
