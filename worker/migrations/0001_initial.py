# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-05-15 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import worker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='Date Publised')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=18)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('Call_Number', models.CharField(help_text='*REQUIRED*', max_length=10)),
                ('WhatsApp', models.CharField(blank=True, help_text='Ignore If Call number is the same for WhatsApp', max_length=10)),
                ('Main_job_description', models.CharField(help_text='e.g Carpenter', max_length=30)),
                ('Other_jobs_description', models.CharField(blank=True, max_length=50)),
                ('Region', models.CharField(choices=[('GA', 'Greater Accra Region'), ('CR', 'Central Region'), ('WR', 'Western Region'), ('ER', 'Eastern Region'), ('VR', 'Volta Region'), ('AS', 'Ashanti Region'), ('BA', 'Brong Ahafo Region'), ('NR', 'Northern Region'), ('UE', 'Upper East Region'), ('UW', 'Upper West Region')], default='GA', max_length=2)),
                ('City_or_Town', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('profile_Picture', models.FileField(upload_to=worker.models.get_upload_file_name)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.Worker'),
        ),
    ]
