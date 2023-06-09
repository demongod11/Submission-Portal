# Generated by Django 4.2 on 2023-05-02 03:10

import coursemanager.models
import coursemanager.storage
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursemanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Assignment Name')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Deadline')),
                ('max_marks', models.IntegerField(blank=True, null=True, verbose_name='Maximum Marks')),
                ('assignment_file', models.FileField(blank=True, null=True, storage=coursemanager.storage.OverwriteStorage(), upload_to=coursemanager.models.assignment_upload_file_name, verbose_name='Assignment File')),
                ('created_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Created Time')),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Student Name')),
                ('roll_number', models.CharField(blank=True, max_length=256, null=True, verbose_name='Roll Number')),
                ('submission_file', models.FileField(blank=True, null=True, storage=coursemanager.storage.OverwriteStorage(), upload_to=coursemanager.models.submission_upload_file_name, verbose_name='Assignment File')),
                ('submitted_assignment', models.CharField(blank=True, max_length=256, null=True, verbose_name='Submitted To')),
                ('is_graded', models.BooleanField(default=False)),
                ('marks', models.IntegerField(blank=True, null=True, verbose_name='Marks Obtained')),
                ('feedback', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Feedback')),
                ('submission_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Submission Time')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemanager.siteuser')),
            ],
        ),
    ]
