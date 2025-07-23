# Import Python's built-in csv module to handle CSV file creation
import csv

# Import BaseCommand to create a custom management command
from django.core.management.base import BaseCommand

# Import apps module to dynamically fetch models from all installed apps
from django.apps import apps

# Import datetime module to generate timestamps for the exported file name
import datetime

# Define the custom management command class
# Proposed usage: python manage.py exportdata <model_name>
class Command(BaseCommand):
    # Description of the command (visible with 'python manage.py help exportdata')
    help = "Export data from the database to a CSV file"
    
    # Define command-line arguments for this command
    def add_arguments(self, parser):
        # Positional argument: model_name (expects the name of the model to export)
        parser.add_argument('model_name', type=str, help="Model name")
    
    # Logic to execute when the command runs
    def handle(self, *args, **kwargs):
        # Get the model name passed as a command-line argument and capitalize it for consistency
        model_name = kwargs['model_name'].capitalize()
        
        # Initialize the model variable to None
        model = None
        # Search through all installed apps for the specified model
        for app_config in apps.get_app_configs():
            try:
                # Try to fetch the model from the current app
                model = apps.get_model(app_config.label, model_name)
                break # Stop searching once the model is found
            except LookupError:
                # If model is not found in this app, continue to the next app
                pass
        
        # If the model is still None, print an error and stop execution
        if not model:
            self.stderr.write(f"Model {model_name} could not found")
            return
        
        # Fetch all records from the model's database table
        data = model.objects.all()
        
        # Generate a timestamp (format: YYYY-MM-DD-HH-MM-SS) for unique file naming
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        # Define the CSV file name/path, including model name and timestamp
        file_path = f"exported_{model_name}_data_{timestamp}.csv"
        
        # Open the CSV file in write mode ('w') and prevent blank lines using newline=''
        with open(file_path, 'w', newline='') as file:
             # Create a CSV writer object
            writer = csv.writer(file)
            
            # Write the CSV header (column names)
            # Get all field names of the model dynamically using model._meta.fields
            writer.writerow([field.name for field in model._meta.fields])
            
            # Write each row of data to the CSV
            for dt in data:
                # For each object, fetch the value of every field and write as a row
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        
        # Print success message in green text to indicate successful export
        self.stdout.write(self.style.SUCCESS("Data exported successfully!"))