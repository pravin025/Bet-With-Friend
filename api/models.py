from django.db import models
from django.contrib.auth.models import User


def image_upload_handler(instance, file_name):
    return f'avatar/{instance.user.id}/{file_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_handler, blank=True)
    is_premium = models.BooleanField(default=False)
    bio = models.CharField(max_length=256, blank=True, null=True)


class Group(models.Model):
    name = models.CharField(max_length=32, null=False, unique=False)
    location = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=256, null=False, unique=False)

    class Meta:
        unique_together = ('name', 'location')


class Event(models.Model):
    team1 = models.CharField(max_length=32, blank=False)
    team2 = models.CharField(max_length=32, blank=False)
    time = models.DateTimeField(null=False, blank=False)
    score1 = models.IntegerField(null=True, blank=True)
    score2 = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(Group, related_name='events', on_delete=models.CASCADE)
