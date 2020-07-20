from django.db import models


# Create your models here.
class DummyModal(models.Model):
    name = models.CharField(max_length=80)
