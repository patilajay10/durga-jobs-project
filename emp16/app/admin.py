from django.contrib import admin
from app.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
 list_display=['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)

#we have register model inside admin.py
#we register model class inside admin.py so that it is available inside admin interface

