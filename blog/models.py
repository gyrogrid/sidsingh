from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.CharField(max_length=100000)
	date = models.DateTimeField('date published')
	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post)
	body = models.CharField(max_length=1000)
	date = models.DateTimeField('date published')
	def __str__(self):
		return self.id
