# Generated by Django 4.2.7 on 2023-11-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentrequest', '0003_subject_year_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='year_level',
        ),
        migrations.AddField(
            model_name='subject',
            name='year_level',
            field=models.ManyToManyField(blank=True, null=True, related_name='year_level', to='studentrequest.yearlevel'),
        ),
    ]
