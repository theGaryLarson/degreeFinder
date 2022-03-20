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

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Degree'
        verbose_name_plural = 'Degrees'


