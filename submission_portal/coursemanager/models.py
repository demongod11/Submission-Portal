import os
from .storage import OverwriteStorage
from django.core.exceptions import ValidationError
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import channels.layers
from django.dispatch import receiver
from asgiref.sync import async_to_sync
import json
from channels.layers import get_channel_layer


def assignment_upload_file_name(instance, filename):
    return 'assignments/{0}'.format(filename)

def submission_upload_file_name(instance, filename):
    return 'submissions/{0}_{1}'.format(instance.student.pk, filename)

    
# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Assignment(models.Model):
    assignment_name = models.CharField('Assignment Name', max_length=256, null=True, blank=True)
    description = models.CharField('Description', max_length=1024, null=True, blank=True)
    deadline = models.DateTimeField('Deadline', null=True, blank=True)
    max_marks = models.IntegerField('Maximum Marks', null=True, blank=True)
    assignment_file = models.FileField('Assignment File', upload_to=assignment_upload_file_name, storage=OverwriteStorage(), null=True, blank=True)
    created_time = models.DateTimeField('Created Time', default=datetime.datetime.now, null=True, blank=True)

    def assignment_file_url(self):
        return 'assignments/{0}'.format(self.assignment_file)

class SubmittedAssignment(models.Model):
    student = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True)
    student_name = models.CharField('Student Name', max_length=256, null=True, blank=True)
    roll_number = models.CharField('Roll Number', max_length=256, null=True, blank=True)
    submission_file = models.FileField('Submission File', upload_to=submission_upload_file_name, storage=OverwriteStorage(), null=True, blank=True)
    submitted_assignment_name = models.CharField('Submitted To', max_length=256, null=True, blank=True)
    submitted_assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True)
    is_graded = models.BooleanField(default=False)
    marks = models.IntegerField('Marks Obtained', null=True, blank=True)
    feedback = models.CharField('Feedback', max_length=1024, null=True, blank=True)
    submission_time = models.DateTimeField('Submission Time', default=datetime.datetime.now, null=True, blank=True)


@receiver(post_save, sender=Assignment)
def assign_created_handler(sender, instance,created , **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data  = {'message': 'New Assignment Uploaded!! - ' + instance.assignment_name}
        async_to_sync(channel_layer.group_send)(
            'channel_group',{
                'type': 'notif_send',
                'value': json.dumps(data)
            }
        )
    if not created:
        channel_layer = get_channel_layer()
        data  = {'message': instance.assignment_name + ' has been updated'}
        async_to_sync(channel_layer.group_send)(
            'channel_group',{
                'type': 'notif_send',
                'value': json.dumps(data)
            }
        )

@receiver(post_save, sender=SubmittedAssignment)
def assign_created_handler(sender, instance,created , **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data  = {'message': instance.student_name + " has submitted " + instance.submitted_assignment_name}
        async_to_sync(channel_layer.group_send)(
            'channel_group_instructor',{
                'type': 'notif_send',
                'value': json.dumps(data)
            }
        )
    if not created:
        channel_layer = get_channel_layer()
        data  = {'message': 'Your submission for ' + instance.submitted_assignment_name + ' has been graded'}
        async_to_sync(channel_layer.group_send)(
            'channel_group',{
                'type': 'notif_send',
                'value': json.dumps(data)
            }
        )