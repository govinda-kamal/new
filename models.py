from django.db import models

# Create your models here.
class Post(models.Model) :
    s_no= models.AutoField(primary_key=True)
    Title=models.TextField(max_length=200,default="")
    Content=models.CharField(max_length=1000,default="")
    slug=models.CharField(max_length=130,default="")    # slug is url 
    Author=models.CharField(max_length=20,default="")
    Date=models.DateField(blank=True)

    def __str__(self) :
        return self.Title + " by " + self.Author