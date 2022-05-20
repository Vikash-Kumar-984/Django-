from django.db import models

# makemigrations is used to create changes and store in a file
# migrate is used to apply the pending changes by makemigrations

# Create your models here.                                                                  
class Contact(models.Model):
    name=models.CharField(max_length=136)
    email=models.CharField(max_length=36)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name