from django.db import models
from .data_file import DataFile

class Video(DataFile):
    suffix = models.CharField(max_length=255)
    fps = models.FloatField()
    duration = models.FloatField()
    width = models.IntegerField()
    height = models.IntegerField()
