# Generated by Django 3.2.4 on 2022-10-04 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Encounter', '0012_remove_guardian_guardiansex'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guardian',
        ),
    ]
