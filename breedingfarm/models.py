from django.db import models
class Homepage(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    background_image1 = models.ImageField(upload_to='homepage/', default='homepage.jpg')

    def __str__(self):
        return self.heading

class About(models.Model):
    story = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    image = models.ImageField(upload_to='about/', default='about/farm-default.jpg')

    def __str__(self):
        return "About KQ3 Meadows"

class Founder(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='founders/', default='founders/default.jpg')

    def __str__(self):
        return self.name
