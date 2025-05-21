from django.core.management.base import BaseCommand
from myapp.models import Comment

class Command(BaseCommand):
    help = 'Delete all comments from the database'

    def handle(self, *args, **kwargs):
        Comment.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All comments have been deleted.'))