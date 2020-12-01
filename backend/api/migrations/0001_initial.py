# Generated by Django 2.2.4 on 2020-06-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('date', models.TextField(blank=True)),
                ('applicant', models.TextField(blank=True)),
                ('status', models.TextField(blank=True)),
                ('data', models.TextField(blank=True)),
                ('validator', models.TextField(blank=True)),
                ('verify_time', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
                ('site', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('user', models.TextField(blank=True)),
                ('cc', models.TextField(blank=True)),
                ('data', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'edit',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('group_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
                ('caption', models.TextField(blank=True)),
                ('authority', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('members', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('info_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('sn', models.IntegerField(blank=True)),
                ('func_uid', models.TextField(blank=True)),
                ('version', models.TextField(blank=True)),
                ('issued', models.TextField(blank=True)),
                ('expiration', models.TextField(blank=True)),
                ('count', models.IntegerField(blank=True)),
                ('registration', models.TextField(blank=True)),
                ('type', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('contact', models.TextField(blank=True)),
                ('info', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'info',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('module_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('category', models.IntegerField(blank=True)),
                ('mod_uid', models.TextField(blank=True)),
                ('caption', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
                ('caption', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Sn',
            fields=[
                ('my_id', models.IntegerField(blank=True, db_column='my_id', primary_key=True, serialize=False, unique=True)),
                ('sn_id', models.IntegerField(blank=True, db_column='id')),
                ('sn', models.IntegerField(blank=True)),
                ('region', models.TextField(blank=True)),
                ('user', models.TextField(blank=True)),
                ('record', models.TextField(blank=True)),
                ('note1', models.TextField(blank=True)),
                ('note2', models.TextField(blank=True)),
                ('note3', models.TextField(blank=True)),
                ('note4', models.TextField(blank=True)),
                ('note5', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'sn',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(blank=True, db_column='id', primary_key=True, serialize=False, unique=True)),
                ('user', models.TextField(blank=True)),
                ('password', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('groups', models.TextField(blank=True)),
                ('region', models.TextField(blank=True)),
                ('record', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]