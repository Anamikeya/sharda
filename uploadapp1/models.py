from django.db import models

# Create your models here.
class files(models.Model):
    image = models.ImageField(upload_to = 'pics/')
    



