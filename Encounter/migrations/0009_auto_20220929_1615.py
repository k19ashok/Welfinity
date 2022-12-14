# Generated by Django 3.2.4 on 2022-09-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Encounter', '0008_medicalproblems_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ros',
            name='abnormalmammogram',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='anorexia',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='apnea',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='arrythmia',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='asthma',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='biopsy',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='blindspots',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='breastmass',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='changeinvision',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='chestpain',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='chills',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='copd',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='cough',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='discharge',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='doe',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='doublevision',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='edema',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='excessivetearing',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='eyepain',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='familyhistoryofglaucoma',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='fatigue',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='fever',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='frequentcolds',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='hearingloss',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='heartproblem',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='heatorcold',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='hemoptysis',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='historyofheartmurmur',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='insomnia',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='intolerence',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='irritability',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='irritation',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='legpain',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='nightsweats',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='nosebleed',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='orthopnea',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='pain',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='palpitation',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='peripheral',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='photophobia',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='pnd',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='postnasaldrip',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='redness',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='shortnessofbreath',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='sinusproblem',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='snoring',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='sorethroat',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='sputum',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='syncope',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='tinnitus',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='vertigo',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='weakness',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='weightchange',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ros',
            name='wheezing',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
