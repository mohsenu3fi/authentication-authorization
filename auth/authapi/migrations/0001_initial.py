# Generated by Django 3.2.5 on 2021-07-25 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('email', models.EmailField(default=None, max_length=30, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('usertype', models.CharField(max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(default=None, max_length=30)),
                ('last_name', models.CharField(default=None, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_wms', models.BooleanField(default=False)),
                ('access_supplyf', models.BooleanField(default=False)),
                ('access_catalog', models.BooleanField(default=False)),
                ('access_crm', models.BooleanField(default=False)),
                ('access_rshipment', models.BooleanField(default=False)),
                ('wms_pages', models.CharField(default=None, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
