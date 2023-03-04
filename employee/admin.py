from django.contrib import admin

# Register your models here.
from employee.models import Employee

# registering Employee table/model
admin.site.register(Employee)