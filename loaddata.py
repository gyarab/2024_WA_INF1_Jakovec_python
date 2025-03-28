import os
from django.core.management import call_command
from django.conf import settings

# Ensure the Django settings module is configured
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'databaze_punku.settings')

# Now we can import Django and call commands
import django
django.setup()

# Run the dumpdata command
with open('music_data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'myapp.band', 'myapp.album', 'myapp.song', indent=4, stdout=f)
