from django.db import models

class jobs(models.Model):
	status = models.IntegerField(default=0)