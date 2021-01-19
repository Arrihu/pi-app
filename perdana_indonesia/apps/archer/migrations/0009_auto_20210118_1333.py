# Generated by Django 2.2.17 on 2021-01-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archer', '0008_auto_20210118_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archer',
            name='qrcode',
        ),
        migrations.AddField(
            model_name='archerapprovaldocument',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='qr_code/%Y/%m/%d'),
        ),
    ]