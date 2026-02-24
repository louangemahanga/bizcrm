from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apps.crm.models import Prospect


class Command(BaseCommand):
    help = 'Crée les groupes Manager et Commercial avec leurs permissions'

    def handle(self, *args, **kwargs):

        prospect_ct = ContentType.objects.get_for_model(Prospect)

        # Permissions disponibles
        can_view   = Permission.objects.get(codename='view_prospect',   content_type=prospect_ct)
        can_add    = Permission.objects.get(codename='add_prospect',    content_type=prospect_ct)
        can_change = Permission.objects.get(codename='change_prospect', content_type=prospect_ct)
        can_delete = Permission.objects.get(codename='delete_prospect', content_type=prospect_ct)

        # Groupe Manager — accès complet
        manager_group, created = Group.objects.get_or_create(name='Manager')
        manager_group.permissions.set([can_view, can_add, can_change, can_delete])
        self.stdout.write(self.style.SUCCESS('✅ Groupe Manager créé'))

        # Groupe Commercial — pas de suppression
        commercial_group, created = Group.objects.get_or_create(name='Commercial')
        commercial_group.permissions.set([can_view, can_add, can_change])
        self.stdout.write(self.style.SUCCESS('✅ Groupe Commercial créé'))