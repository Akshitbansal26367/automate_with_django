# Import BaseCommand to create a custom Django management command
from django.core.management.base import BaseCommand

# Import the Student model from the app "dataentry"
from dataentry.models import Student

# Define your custom command class
class Command(BaseCommand):
    # This is the description of your command (shown in "python manage.py help")
    help = "It will insert data to the database"
    
    # The handle() method is called automatically when the command runs
    def handle(self, *args, **kwargs):
        # Create a dataset of student records to insert into the database 
        dataset = [
            {'roll_no': 1002, 'name': 'Sachin', 'age': 21},
            {'roll_no': 1003, 'name': 'John', 'age': 22},
            {'roll_no': 1004, 'name': 'Mike', 'age': 23},
        ]
        
        # Loop through each dictionary in the dataset
        for data in dataset:
            # Create and save a Student object using the data
            Student.objects.create(
                roll_no=data['roll_no'],  # Set roll_no field
                name= data['name'],  # Set name field
                age=data['age']  # Set age field
            )
            
        # Print a success message after all data is inserted
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))