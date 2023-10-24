# Generated by Django 2.2.27 on 2022-03-17 11:47

from django.db import migrations, models

from NEMO.migrations_utils import create_news_for_version


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0037_version_3_16_0'),
    ]

    def new_version_news(apps, schema_editor):
        create_news_for_version(apps, "4.0.0", "")

    def add_modbus_tcp_interlock_category(apps, schema_editor):
        InterlockCardCategory = apps.get_model("NEMO", "InterlockCardCategory")
        InterlockCardCategory.objects.create(name="ModbusTcp", key="modbus_tcp")

    operations = [
        migrations.RunPython(new_version_news),
        migrations.RunPython(add_modbus_tcp_interlock_category),
        migrations.AlterField(
            model_name='interlock',
            name='channel',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Channel/Relay/Coil'),
        ),
    ]
