from django.contrib import admin
from .models import Admin, Employee, Settings, Record

admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Settings)
admin.site.register(Record)