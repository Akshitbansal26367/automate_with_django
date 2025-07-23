from django.apps import apps  # Import Django's apps registry to access all models

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