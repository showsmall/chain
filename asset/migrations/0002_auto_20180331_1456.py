# Generated by Django 2.0.3 on 2018-03-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_user',
            name='private_key',
            field=models.FileField(blank=True, null=True, upload_to='upload/privatekey/%Y%m%d6679', verbose_name='私钥'),
        ),
    ]