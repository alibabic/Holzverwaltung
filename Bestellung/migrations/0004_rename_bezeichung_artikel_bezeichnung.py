# Generated by Django 5.1.3 on 2024-12-10 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bestellung', '0003_alter_artikel_bezeichung'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='bezeichung',
            new_name='bezeichnung',
        ),
    ]