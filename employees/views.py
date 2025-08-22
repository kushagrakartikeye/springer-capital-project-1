from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from .models import Employee, Performance
from .serializers import EmployeeSerializer, PerformanceSerializer
from departments.models import Department
from attendance.models import Attendance
from datetime import datetime, timedelta


# Employee API ViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['department', 'date_of_joining']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'date_of_joining']


# Performance API ViewSet
class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['rating', 'review_date']
    search_fields = ['employee__name']
    ordering_fields = ['rating', 'review_date']


# Chart view rendering template with two charts
def charts_view(request):
    departments = Department.objects.annotate(employee_count=Count('employees'))

    six_months_ago = datetime.now() - timedelta(days=180)

    attendance_by_month = (
        Attendance.objects
        .filter(date__gte=six_months_ago)
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    months = [entry['month'].strftime("%b %Y") for entry in attendance_by_month]
    attendance_counts = [entry['count'] for entry in attendance_by_month]

    context = {
        'department_labels': [dept.name for dept in departments],
        'employee_counts': [dept.employee_count for dept in departments],
        'attendance_months': months,
        'attendance_counts': attendance_counts,
    }

    return render(request, 'charts.html', context)
def home_view(request):
    return HttpResponse(
        "<h2>Welcome to the Employee Management API</h2><ul>"
        "<li><a href='/admin/'>Admin</a></li>"
        "<li><a href='/swagger/'>Swagger Documentation</a></li>"
        "<li><a href='/api/charts/'>Charts</a></li>"
        "</ul>"
    )