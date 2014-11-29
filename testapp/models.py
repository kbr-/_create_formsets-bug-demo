from django.db import models


class GoodModel(models.Model):
	name = models.IntegerField(unique=True)

	def __str__(self):
		return str(self.name)

class RelatedToGoodModel(models.Model):
	name = models.IntegerField(unique=True)
	good_model = models.ForeignKey(GoodModel)

	def __str__(self):
		return str(self.name)


class BadModel(models.Model):
	id = models.IntegerField(primary_key=True)

	def __str__(self):
		return str(self.id)


class RelatedToBadModel(models.Model):
	name = models.IntegerField(unique=True)
	bad_model = models.ForeignKey(BadModel)

	def __str__(self):
		return str(self.name)