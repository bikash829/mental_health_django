from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from dashboard.models import *  # Replace with actual models you need permissions for

class Command(BaseCommand):
    help = 'Setup user roles and permissions'

    def handle(self, *args, **kwargs):
        # Define roles
        roles = ('admin', 'doctor', 'counselor', 'patient')

        # Permissions mapping for each role
        # role_permissions = {
        #     'admin': ['add_mymodel', 'change_mymodel', 'delete_mymodel', 'view_mymodel'],  # Full access
        #     'doctor': ['view_mymodel', 'change_mymodel'],  # Can view and update
        #     'counselor': ['view_mymodel'],  # Only view permissions
        #     'patient': ['view_mymodel'],  # Limited view permissions
        # }

        # Create groups and assign permissions
        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            # for perm_code in role_permissions[role]:
            #     permission = Permission.objects.get(codename=perm_code)
            #     group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Roles have been set up.'))
