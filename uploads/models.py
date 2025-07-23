from django.db import models

# Define a model named Upload to store uploaded files and related information
class Upload(models.Model):
    # Field to store the uploaded file
    # upload_to="uploads/" means files will be stored in the 'uploads/' directory inside MEDIA_ROOT
    file = models.FileField(upload_to="uploads/")
    
    # Field to store the name of the model associated with the upload
    # max_length=50 means it can store up to 50 characters
    model_name = models.CharField(max_length=50)
    
    # Field to store the date and time when the file was uploaded
    # auto_now_add=True means this field will automatically be set to the current date & time when the record is created
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # String representation of the Upload object
        # This will return the model_name field when an Upload instance is printed
        return self.model_name