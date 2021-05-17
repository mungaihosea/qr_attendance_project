from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

class Admin(User):
    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Adminisrators"

class Employee(User):
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    def __str__(self):
        return self.username

class Settings(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField(default=8000)

    def __str__(self):
        return self.ip
    
class Record(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length= 30, null = True)
    email = models.EmailField(null = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    activity = CharField(max_length=30, choices=[('check in', 'check in'), ('check out', 'check out')])

    def __str__(self):
        return self.user.username + " " + self.activity