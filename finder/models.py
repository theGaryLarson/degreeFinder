import datetime
from django.db import models


# Create your models here.
class AreaOfStudy(models.Model):
    area_of_study = models.CharField(max_length=500)
    description = models.CharField(null=True, blank=True, max_length=1000)
    revised_date = models.DateField(datetime.date.today())

    def __str__(self):
        return self.area_of_study

    class Meta:
        db_table = 'Area of Study'
        verbose_name_plural = 'Areas of Study'


class Pathway(models.Model):
    area = models.ForeignKey(AreaOfStudy, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True, max_length=1000)
    revised_date = models.DateField(datetime.date.today())

    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'Pathway'
        verbose_name_plural = 'Pathways'


class Degree(models.Model):
    pathway = models.ForeignKey(Pathway, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True, max_length=1000)
    contact = models.CharField(max_length=100)
    guide = models.URLField(null=True, blank=True)
    # a list of grants stored as a json object
    grants = models.JSONField(null=True, blank=True)
    revised_date = models.DateField(datetime.date.today())

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Degree'
        verbose_name_plural = 'Degrees'


# todo: migrate & implement these classes in the project
class Class(models.Model):
    degree = models.ManyToManyField(Degree)
    title = models.CharField(max_length=200, blank=True)
    class_code = models.CharField(max_length=10, blank=True)
    instructor = models.CharField(max_length=100, null=True, blank=True)
    isOnline = models.BooleanField(null=True)
    # Json field will contain quarter, year, daysOfWeek, time
    schedule = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Class'
        verbose_name_plural = 'Classes'


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    ctc_link_id = models.IntegerField(null=True)
    is_enrolled = models.BooleanField(null=True)
    degree = models.ForeignKey(Degree, on_delete=models.DO_NOTHING)
    # will contain a list of pathways of interest
    path_interests = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.last_name + ', ' + self.first_name + 'CTCLINKID: ' + str(self.ctc_link_id)

    class Meta:
        db_table = 'Student'
        verbose_name_plural = 'Students'
