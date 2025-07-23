from django.conf import settings  # To access project settings like BASE_DIR
from django.shortcuts import redirect, render  # To render templates and redirect requests
from .utils import get_all_custom_models  # Utility function to get all custom models
from uploads.models import Upload  # Import Upload model to store uploaded file info
from django.core.management import call_command  # To call a custom Django management command
from django.contrib import messages

# View to handle importing data into database tables
def import_data(request):
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Get the uploaded file from the request
        file_path = request.FILES.get("file_path")
        
        # Get the selected model name from the request
        model_name = request.POST.get("model_name")
        
        # Save the uploaded file and model name in the Upload table
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        
        # Construct the relative path to the uploaded file
        relative_path = str(upload.file.url)  # URL of the uploaded file (relative to MEDIA_URL)
        
        # Get the base directory of the project from settings
        base_url = str(settings.BASE_DIR)
        
        # Combine base path and relative path to get full file path
        file_path = base_url + relative_path
        
        # Call the custom management command 'importdata'
        try:
            # Pass the file_path and model_name as arguments to the command
            call_command("importdata", file_path, model_name)
            messages.success(request, 'Data imported successfully')
        except Exception as e:
            # Raise any exceptions that occur during import
            messages.error(request, str(e))
        
        # Redirect to the same page after processing to avoid form resubmission
        return redirect('import_data')
    else:
        # For GET requests, fetch all custom models to display in the dropdown
        custom_models = get_all_custom_models()
        
        # Pass the list of models to the template context
        context = {
            'custom_models':custom_models
        }
        
    # Render the template with the context
    return render(request, 'dataentry/importdata.html', context)