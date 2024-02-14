from django.contrib import admin
from .models import Employee, Position, Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)
