# Import Django's built-in models module
from django.db import models

# Define a Student model (this will create a table in the database named dataentry_student)
class Student(models.Model):
    # roll_no field: Stores the student's roll number as a string (max length = 10 characters)
    roll_no = models.CharField(max_length=10)
    
    # name field: Stores the student's name as a string (max length = 20 characters)
    name = models.CharField(max_length=20)
    
    # age field: Stores the student's age as an integer
    age = models.IntegerField()
    
    # String representation of the Student object (useful in admin panel and shell)
    def __str__(self):
        # When we print the Student object, it will show the student's name
        return self.name

# Define a Customer model (this will create a table in the database named dataentry_customer)
class Customer(models.Model):
    # customer_name field: Stores the customer's name as a string (max length = 20 characters)
    customer_name = models.CharField(max_length=20)
    
    # country field: Stores the customer's country as a string (max length = 20 characters)
    country = models.CharField(max_length=20)
    
    # String representation of the Customer object (useful in admin panel and shell)
    def __str__(self):
        # When we print the Customer object, it will show the customer's name
        return self.customer_name