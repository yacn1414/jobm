# Generated by Django 3.2.16 on 2023-01-01 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0004_remove_jobs_idemploee'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabtjob',
            name='vaziat',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='sabtjob',
            name='id_employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]