from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # This sets the description shown in "python manage.py help"
    help = "Prints Hello World"
    
    def handle(self, *args, **kwargs):
        """
        This method runs automatically when the command is executed.
        """
        # Print "Hello World" to the console
        self.stdout.write("Hello World")