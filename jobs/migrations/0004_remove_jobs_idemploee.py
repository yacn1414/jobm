# Generated by Django 4.1.4 on 2022-12-30 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobs_idemploee_alter_jobs_idemployer_sabtjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='idemploee',
        ),
    ]
