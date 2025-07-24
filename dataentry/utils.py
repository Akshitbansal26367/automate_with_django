from django.apps import apps  # Import Django's apps registry to access all models
from django.core.management.base import CommandError
import csv
from django.db import DataError
from django.core.mail import EmailMessage
from django.conf import settings

# Function to retrieve all custom models in the project
def get_all_custom_models():
    # List of default Django models to exclude from the result
    default_models = ['ContentType', 'Session', 'LogEntry', 'Group', 'Permission', 'User', 'Upload']
    
    # Initialize an empty list to store custom model names
    custom_models = []
    
    # Iterate through all models registered in the project
    for model in apps.get_models():
        # Check if the model name is NOT in the list of default models
        if model.__name__ not in default_models:
            # Add the model name to the custom_models list
            custom_models.append(model.__name__)
    
    # Return the list of custom model names
    return custom_models

def check_csv_errors(file_path, model_name):
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
        
        # get all the field names of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != "id"]
        
        try:
            # Open the CSV file for reading        
            with open(file_path, 'r') as file:
                # Create a DictReader to parse CSV rows into dictionaries
                reader = csv.DictReader(file)
                csv_header = reader.fieldnames
                
                # compare csv header with model's field names
                if csv_header != model_fields:
                    raise DataError(f"CSV file doesn't match with the {model_name} table fields.")
        except Exception as e:
            raise e
        
        return model

def send_email_notification(mail_subject, message, to_email):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
        mail.send()
    except Exception as e:
        raise e