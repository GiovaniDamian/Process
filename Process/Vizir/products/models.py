from django.db import models


class telzir(models.Model):
    eo = models.FloatField(max_length=1)
    ed = models.FloatField(max_length=1)
    min = models.FloatField()
    ofm = models.FloatField(max_length=1)
