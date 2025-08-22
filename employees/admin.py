from django.contrib import admin
from .models import Employee, Performance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'date_of_joining')
    list_filter = ('department',)
    search_fields = ('name', 'email')

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'rating', 'review_date')
    list_filter = ('rating',)
