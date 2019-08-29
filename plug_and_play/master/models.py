from django.db import models

class jobs(models.Model):
	status = models.IntegerField(default=0)

class task(models.Model):
	taskid = models.IntegerField(default=0)
	jobid = models.IntegerField(default=0)
	workerid = models.IntegerField(default=0)
	status = models.IntegerField(default=0)