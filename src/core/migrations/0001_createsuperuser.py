import os

from django.contrib.auth.models import User
from django.db import migrations


def createsuperuser(apps, schema_editor):
    kinideas_profile_admin_password = "playground"
    User.objects.create_superuser("admin", password=kinideas_profile_admin_password)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(createsuperuser)
    ]