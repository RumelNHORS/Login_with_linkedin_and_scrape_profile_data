from django.db import models


class Experience(models.Model):
    organisation_profile = models.URLField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # start_time = models.CharField(max_length=100, blank=True, null=True)
    # end_time = models.CharField(max_length=100,  blank=True, null=True)
    # duration = models.CharField(max_length=50, blank=True, null=True)

class UserProfile(models.Model):
    profile = models.CharField(max_length=200)
    url = models.URLField()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    followers = models.CharField(max_length=50, blank=True, null=True)
    connections = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    experience = models.ManyToManyField(Experience)
    education = models.ManyToManyField('Education', blank=True)

class Education(models.Model):
    organisation = models.CharField(max_length=100, blank=True)
    organisation_profile = models.URLField(blank=True)
    course_details = models.TextField()
    description = models.TextField(blank=True)
    # start_time = models.CharField(max_length=100)
    # end_time = models.CharField(max_length=100)