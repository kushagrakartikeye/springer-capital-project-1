from django.urls import path
from rest_framework import routers
from .views import EmployeeViewSet, PerformanceViewSet, charts_view

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('charts/', charts_view, name='charts'),
]

urlpatterns += router.urls
