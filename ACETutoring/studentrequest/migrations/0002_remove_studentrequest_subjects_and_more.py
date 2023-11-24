# Generated by Django 4.2.7 on 2023-11-18 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentrequest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentrequest',
            name='subjects',
        ),
        migrations.AddField(
            model_name='studentrequest',
            name='subject 1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject1', to='studentrequest.subject'),
        ),
        migrations.AddField(
            model_name='studentrequest',
            name='subject 2 (optional)',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='studentrequest.subject'),
        ),
        migrations.AddField(
            model_name='studentrequest',
            name='subject 3 (optional)',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject3', to='studentrequest.subject'),
        ),
        migrations.AddField(
            model_name='studentrequest',
            name='subject 4 (optional)',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject4', to='studentrequest.subject'),
        ),
    ]