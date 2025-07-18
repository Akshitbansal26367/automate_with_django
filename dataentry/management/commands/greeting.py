from django.core.management.base import BaseCommand

# Custom management command: python manage.py greeting <name>
class Command(BaseCommand):
    help = "Greets the user"  # This shows up when you do python manage.py help
    
    def add_arguments(self, parser):
        """
        This method lets you add command line arguments to your command.
        Here we're adding one positional argument: name
        """
        parser.add_argument(
            "name",  # Positional argument (mandatory)
            type=str,  # Type of the argument
            help="Specifies user name"  # Help text
        )
    
    def handle(self, *args, **kwargs):
        """
        This is the method that runs when your command is executed.
        """
        name = kwargs['name']  # Get the value of the 'name' argument
        greeting = f"Hi {name}, Good Morning!"
        
        # Output the result with success styling (green text in terminal)
        self.stdout.write(self.style.SUCCESS(greeting))