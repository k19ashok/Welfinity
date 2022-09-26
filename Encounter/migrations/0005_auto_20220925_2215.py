# Generated by Django 3.2.4 on 2022-09-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Encounter', '0004_clinicalnotes_ros_soap_vitals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitals',
            name='bmi',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='bpdiastolic',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='bpsystolic',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='headcircumference',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='inhaledoxygenconc',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='oxygenflowrate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='oxygensaturation',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='pediatricbmipercentile',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='pulse',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='respiration',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='waistcircumference',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, max_length=3, null=True),
        ),
    ]
