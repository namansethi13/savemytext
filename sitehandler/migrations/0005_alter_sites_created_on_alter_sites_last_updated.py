# Generated by Django 4.0.3 on 2022-09-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0004_page_remove_sites_cipher_sites_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='created_on',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='sites',
            name='last_updated',
            field=models.DateTimeField(),
        ),
    ]
