from django.core.management.base import BaseCommand
from django.conf import settings
from django_compiler.utils import compile_directory

class Command(BaseCommand):
    help = 'Compiles python files in a directory'

    def add_arguments(self, parser):
        parser.add_argument(
            '--exclude-dirs',
            nargs='*',
            help='Directories to exclude from compilation',
        )

    def handle(self, *args, **options):
        exclude_dirs = ["django_compiler", "env"]
        directory = settings.BASE_DIR
        compile_directory(directory, exclude_dirs=exclude_dirs)
