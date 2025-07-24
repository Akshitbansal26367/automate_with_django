from django.urls import path  # Import Django's path function to define URL patterns
from . import views  # Import views from the current app

# Define URL patterns for this app
urlpatterns = [
    # URL pattern for importing data
    # When the user visits "import-data/", the import_data view will be called
    # The name 'import_data' allows reverse URL lookups in templates and views
    path("import-data/", views.import_data, name='import_data'),
    path("export-data/", views.export_data, name='export_data'),
]