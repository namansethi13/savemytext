# Generated by Django 4.1 on 2022-09-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0002_alter_sites_site_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
