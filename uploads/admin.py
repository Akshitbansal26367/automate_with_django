from django.contrib import admin  # Import Django's admin module
from .models import Upload  # Import the Upload model from the current app's models

# Define a custom admin class for the Upload model
class UploadAdmin(admin.ModelAdmin):
    # list_display defines which fields to show in the admin list view for Upload
    list_display = ['model_name', 'uploaded_at']

# Register the Upload model with the admin site using the custom UploadAdmin class
admin.site.register(Upload, UploadAdmin)