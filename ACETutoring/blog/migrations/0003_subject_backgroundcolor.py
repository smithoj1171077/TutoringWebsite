# Generated by Django 4.2.7 on 2023-11-16 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_subject_image_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='backgroundColor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]