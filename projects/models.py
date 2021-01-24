from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")

class Comment(models.Model):
    author = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    