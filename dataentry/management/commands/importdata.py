# Import BaseCommand to create a custom management command
# Import CommandError to raise errors in case something goes wrong
from django.core.management.base import BaseCommand, CommandError

# Import apps module to dynamically fetch models from all installed apps
from django.apps import apps

# Import Python's built-in csv module for reading CSV files
import csv

# Define the custom management command class
# Proposed usage: python manage.py importdata file_path model_name
class Command(BaseCommand):
    # Description of the command. Appears in "python manage.py help importdata"
    help = "Import data from CSV file"
    
    # Define command-line arguments for this command
    def add_arguments(self, parser):
        # Positional argument for file path: expects a string value
        parser.add_argument("file_path", type=str, help="Path to the CSV file")
        # Positional argument for model name: expects a string value
        parser.add_argument("model_name", type=str, help="Name of the model")
    
     # This method contains the logic executed when the command is run
    def handle(self, *args, **kwargs):
        # Retrieve command-line arguments
        file_path = kwargs['file_path']  # Path to the CSV file
        model_name = kwargs['model_name'].capitalize()  # Capitalize model name for consistency
        
        # Initialize model to None
        model = None
        
        # Search for the model across all installed apps
        for app_config in apps.get_app_configs():
            try:
                # Try to get the model from the current app
                model = apps.get_model(app_config.label, model_name)
                break # Model found, exit the loop
            except LookupError:
                # Model not found in this app, continue to the next one
                continue
        
        # If model is still None, raise an error as it was not found
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')
        
        # Open the CSV file for reading        
        with open(file_path, 'r') as file:
            # Create a DictReader to parse CSV rows into dictionaries
            reader = csv.DictReader(file)
            
            # Loop through each row in the CSV file
            for row in reader:
                # Create a new instance of the model using row data
                # Assumes CSV headers match model field names
                model.objects.create(**row)
        
        # Print success message to console using Django's SUCCESS styling
        self.stdout.write(self.style.SUCCESS("Data imported from CSV successfully!"))