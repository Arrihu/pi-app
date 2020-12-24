# Generated by Django 2.2.17 on 2020-12-24 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0002_auto_20201224_0454'),
        ('archer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archer',
            name='kecamatan',
        ),
        migrations.AddField(
            model_name='archer',
            name='kelurahan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.Kelurahan'),
        ),
    ]