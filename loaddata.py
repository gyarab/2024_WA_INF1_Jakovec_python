import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'databaze_punku.settings')

django.setup()

call_command('loaddata', 'music_data.json')
