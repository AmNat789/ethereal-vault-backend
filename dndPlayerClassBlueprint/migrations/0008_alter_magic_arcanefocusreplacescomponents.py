# Generated by Django 3.2.7 on 2021-09-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndPlayerClassBlueprint', '0007_alter_magic_cast_at_will'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magic',
            name='arcaneFocusReplacesComponents',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
