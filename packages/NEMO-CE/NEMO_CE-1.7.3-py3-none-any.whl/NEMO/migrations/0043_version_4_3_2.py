# Generated by Django 3.2.16 on 2022-12-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0042_version_4_3_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalaccesslevel',
            name='allow_staff_access',
            field=models.BooleanField(default=False, help_text='Check this box to allow access to Staff and User Office members without explicitly granting them access'),
        ),
    ]
