from django.contrib.gis.db import models
from api.models import UserBase

class Occurrence(models.Model):
	TYPES = [
		(1,'CONSTRUCTION'),
		(2,'SPECIAL_EVENT'),
		(3,'INCIDENT'),
		(4,'WHEATHER_CONDITION'),
		(5,'ROAD_CONDITION'),
	]
	statuses = [
		(1,'TO_BE_VALIDATED'),
		(2,'VALIDATED'),
		(3,'RESOLVED'),
	]
	eyedee = models.AutoField(primary_key=True)
	description = models.CharField(max_length=500)
	location = models.PointField()
	creator = models.ForeignKey(UserBase, on_delete=models.CASCADE)
	creation_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField(choices=statuses)
	category = models.SmallIntegerField(choices=TYPES)

	def set_creator(self,c):
		self.creator=c

	def __str__(self):
		return "{}".format(self.description)