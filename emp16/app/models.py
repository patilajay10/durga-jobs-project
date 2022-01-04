from django.db import models

# Create your models here.
class Employee(models.Model):
 eno=models.IntegerField()
 ename=models.CharField(max_length=30)
 esal=models.FloatField()
 eaddr=models.CharField(max_length=30)
 def __str__(self):
  return 'Employee Object with eno:+str(self.no)'
 

#py manage.py makemigrations
#py manage.py sqlmigrate APPNAME 0001
#py manage.py createsuperuser
#next we have to register Model inside admin interface
#faker:=
#--------     to create fake data
#pip install faker
#fake=faker.Faker()
#
#
#