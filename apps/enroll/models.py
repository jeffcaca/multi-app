from __future__ import unicode_literals

from django.db import models
from ..registration.models import User
# Create your models here.


class Course(models.Model):
	userlinks = models.ManyToManyField(User)
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
