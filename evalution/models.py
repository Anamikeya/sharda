from django.db import models
from .models import models
# Create your models here.
class data(models.Model):
    Full_Name = models.CharField(max_length=100)
    System_id = models.CharField(max_length = 100)
    Roll_No = models.CharField(max_length = 100)
    Email = models.EmailField()
    Project_Title = models.CharField(max_length=100)
    Guide_Name = models.CharField(max_length=100)
    Team_Size = models.IntegerField()
    Project_Category = models.CharField(max_length=100)
    Section = models.CharField(max_length=100)
    Project_Passcode = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length = 100)
    Submitted_Sypnosis = models.CharField(max_length=10)
   
    
    class Meta:
        db_table="evalution_data"
