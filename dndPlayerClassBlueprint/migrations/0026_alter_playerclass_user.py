# Generated by Django 3.2.7 on 2022-01-11 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dndPlayerClassBlueprint', '0025_auto_20220111_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerclass',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
