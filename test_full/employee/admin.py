from django.contrib import admin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'hire_date', 'salary', 'department')
