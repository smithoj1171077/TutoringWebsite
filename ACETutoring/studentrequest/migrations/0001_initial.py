# Generated by Django 4.2.7 on 2023-11-17 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('backgroundColor', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='subject_images')),
            ],
            options={
                'verbose_name_plural': 'subjects',
                'ordering': ('subject',),
            },
        ),
        migrations.CreateModel(
            name='YearLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student name', models.CharField(max_length=255)),
                ('parent/guardian email', models.CharField(max_length=255)),
                ('parent/guardian name', models.CharField(max_length=255)),
                ('students email', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('online only', models.BooleanField()),
                ('are you parent/guardian', models.BooleanField()),
                ('phone number', models.CharField(max_length=10)),
                ('subjects', models.ManyToManyField(to='studentrequest.subject')),
                ('year level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentrequest.yearlevel')),
            ],
        ),
    ]
