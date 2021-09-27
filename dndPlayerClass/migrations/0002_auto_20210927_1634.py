# Generated by Django 3.2.7 on 2021-09-27 14:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dndPlayerClass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('given_languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, size=None)),
                ('additional_languages', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='playerclass',
            name='languagesID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dndPlayerClass.languages'),
        ),
    ]
