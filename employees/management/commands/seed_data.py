from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from departments.models import Department
from employees.models import Employee, Performance
from attendance.models import Attendance

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with employees, departments, performance, and attendance records.'

    def handle(self, *args, **kwargs):
        # Clear existing data (optional, or add your own handling)
        Employee.objects.all().delete()
        Department.objects.all().delete()
        Attendance.objects.all().delete()
        Performance.objects.all().delete()

        # Create Departments
        department_names = ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales']
        departments = []
        for name in department_names:
            dept = Department.objects.create(name=name)
            departments.append(dept)

        # Create Employees
        employees = []
        for _ in range(40):  # Adjust as needed (manager requires 30-50)
            department = random.choice(departments)
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()[:20],  # truncate to max 20 chars to fit DB
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-4y', end_date='today'),
                department=department
            )
            employees.append(employee)

            # Create Performance reviews
            for _ in range(random.randint(1, 3)):
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date=employee.date_of_joining, end_date='today')
                )

            # Create attendance records for recent days
            for _ in range(random.randint(10, 30)):
                status = random.choice(['P', 'A', 'L'])
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-90d', end_date='today'),
                    status=status
                )

        self.stdout.write(self.style.SUCCESS('Seed data created successfully!'))
