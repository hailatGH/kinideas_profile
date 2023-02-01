# Generated by Django 4.1.4 on 2023-01-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPodcastReleased', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NoOfSkipsModel',
            fields=[
                ('user_id', models.CharField(max_length=1023, primary_key=True, serialize=False)),
                ('noOfSkips', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['user_id'],
            },
        ),
        migrations.CreateModel(
            name='SubscribedUsersModel',
            fields=[
                ('user_id', models.CharField(max_length=1023, primary_key=True, serialize=False)),
                ('subscription_type', models.CharField(max_length=1023)),
                ('subscription_expiry_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['user_id'],
            },
        ),
        migrations.CreateModel(
            name='UserPrivilegeModel',
            fields=[
                ('user_id', models.CharField(max_length=1023, primary_key=True, serialize=False)),
                ('privilege', models.IntegerField(default=0)),
                ('created_by', models.CharField(max_length=1023)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['user_id'],
            },
        ),
    ]
