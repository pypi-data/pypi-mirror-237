# Generated by Django 3.2.20 on 2023-08-30 21:49

from django.db import migrations, models

import NEMO.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractoragreementdocuments',
            name='document',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=NEMO.utilities.document_filename_upload, verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='procurementdocuments',
            name='document',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=NEMO.utilities.document_filename_upload, verbose_name='Document'),
        ),
    ]
