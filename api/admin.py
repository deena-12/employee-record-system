from django.contrib import admin
from.models import *

class show(admin.ModelAdmin):
    list_display=('employee_id',
        'name',
        'email',
        'department',
        'designation',
        'salary',
        'date_of_joining',)
    ordering=('employee_id',)



admin.site.register(Employee,show)
