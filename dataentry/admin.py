# Import Django's admin module to customize the admin interface
from django.contrib import admin

# Import the Student model from the current app's models.py
from .models import Student, Customer, Employee

# Register the Student model with the Django admin site
# This allows you to view, add, edit, and delete Student records in the admin panel
admin.site.register(Student)

# Register the Customer model with the Django admin site
# This allows you to view, add, edit, and delete Customer records in the admin panel
admin.site.register(Customer)
admin.site.register(Employee)