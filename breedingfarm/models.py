from django.db import models
class Homepage(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    background_image1 = models.ImageField(upload_to='homepage/', default='homepage.jpg')

    def __str__(self):
        return self.heading
