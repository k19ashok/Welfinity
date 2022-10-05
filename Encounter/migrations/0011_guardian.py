# Generated by Django 3.2.4 on 2022-10-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Encounter', '0010_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('guardianID', models.BigAutoField(primary_key=True, serialize=False)),
                ('guardian', models.CharField(blank=True, max_length=255, null=True)),
                ('guardianrelation', models.TextField(blank=True, null=True)),
                ('guardiansex', models.TextField(blank=True, null=True)),
                ('guardianphone', models.TextField(blank=True, null=True)),
                ('guardianemail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]