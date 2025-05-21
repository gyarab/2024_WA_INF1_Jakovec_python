import os
from django.core.management import call_command
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'databaze_punku.settings')

import django
django.setup()

with open('music_data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'myapp.band', 'myapp.album', 'myapp.song', 'myapp.comment', indent=4, stdout=f)
