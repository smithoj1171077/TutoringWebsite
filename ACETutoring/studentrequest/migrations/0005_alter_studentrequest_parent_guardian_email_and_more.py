# Generated by Django 4.2.7 on 2023-11-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentrequest', '0004_remove_subject_year_level_subject_year_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrequest',
            name='parent/guardian email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='phone number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='students email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
