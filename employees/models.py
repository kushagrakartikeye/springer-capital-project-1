from django.db import models
from departments.models import Department

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")

    def __str__(self):
        return f"{self.name} ({self.department})"
class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    rating = models.IntegerField()
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.rating} on {self.review_date}"
