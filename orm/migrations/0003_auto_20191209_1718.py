# Generated by Django 2.2.8 on 2019-12-09 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_basemember_satuan'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubCommiteMember',
            fields=[
                ('basemember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orm.BaseMember')),
                ('position', models.CharField(max_length=100)),
                ('sk_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sk_document', models.FileField(blank=True, null=True, upload_to='docs/sk/%Y/%m/%d')),
                ('periode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Periode')),
            ],
            options={
                'abstract': False,
            },
            bases=('orm.basemember',),
        ),
        migrations.CreateModel(
            name='PengcabCommiteMember',
            fields=[
                ('basemember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orm.BaseMember')),
                ('position', models.CharField(max_length=100)),
                ('sk_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sk_document', models.FileField(blank=True, null=True, upload_to='docs/sk/%Y/%m/%d')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Branch')),
                ('periode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Periode')),
            ],
            options={
                'abstract': False,
            },
            bases=('orm.basemember',),
        ),
        migrations.CreateModel(
            name='PengprovCommiteMember',
            fields=[
                ('basemember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orm.BaseMember')),
                ('position', models.CharField(max_length=100)),
                ('sk_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sk_document', models.FileField(blank=True, null=True, upload_to='docs/sk/%Y/%m/%d')),
                ('periode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Periode')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Province')),
            ],
            options={
                'abstract': False,
            },
            bases=('orm.basemember',),
        ),
        migrations.CreateModel(
            name='RegionalCommiteMember',
            fields=[
                ('basemember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orm.BaseMember')),
                ('position', models.CharField(max_length=100)),
                ('sk_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sk_document', models.FileField(blank=True, null=True, upload_to='docs/sk/%Y/%m/%d')),
                ('periode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Periode')),
                ('regional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Region')),
            ],
            options={
                'abstract': False,
            },
            bases=('orm.basemember',),
        ),
        migrations.CreateModel(
            name='UnitCommiteMember',
            fields=[
                ('basemember_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orm.BaseMember')),
                ('position', models.CharField(max_length=100)),
                ('sk_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sk_document', models.FileField(blank=True, null=True, upload_to='docs/sk/%Y/%m/%d')),
                ('periode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orm.Periode')),
            ],
            options={
                'abstract': False,
            },
            bases=('orm.basemember',),
        ),
        migrations.DeleteModel(
            name='CommiteMember',
        ),
    ]