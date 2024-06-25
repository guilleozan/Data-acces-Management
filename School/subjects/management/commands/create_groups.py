from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from your_app.models import Article  # Ensure you import your models

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        admin_group, created = Group.objects.get_or_create(name='Administrator')
        tutor_group, created = Group.objects.get_or_create(name='Tutor')
        student_group, created = Group.objects.get_or_create(name='Student')

        # Define permissions
        content_type = ContentType.objects.get_for_model(Article)
        
        # Permissions for Administrators
        admin_permissions = [
            Permission.objects.get(codename='add_article', content_type=content_type),
            Permission.objects.get(codename='change_article', content_type=content_type),
            Permission.objects.get(codename='delete_article', content_type=content_type),
            Permission.objects.get(codename='view_article', content_type=content_type),
        ]
        admin_group.permissions.set(admin_permissions)

        # Permissions for Tutors
        tutor_permissions = [
            Permission.objects.get(codename='add_article', content_type=content_type),
            Permission.objects.get(codename='change_article', content_type=content_type),
            Permission.objects.get(codename='view_article', content_type=content_type),
        ]
        tutor_group.permissions.set(tutor_permissions)

        # Permissions for Students
        student_permissions = [
            Permission.objects.get(codename='view_article', content_type=content_type),
        ]
        student_group.permissions.set(student_permissions)

        self.stdout.write(self.style.SUCCESS('Successfully created user groups and assigned permissions.'))`

