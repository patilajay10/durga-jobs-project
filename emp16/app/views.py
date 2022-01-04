from django.shortcuts import render
from app.models import Employee
from django.http import HttpResponse
#inside views.py how to get Employee table data ?
#emp_list=Employee.objects.all()
# Create your views here.
def empview(request):
   emp_list=Employee.objects.all()
   my_dict={"emp_list":emp_list}
   return render(request,'app/emp.html',context=my_dict)
# in html page there will some different type of language is used i.e. jinja2 templating language