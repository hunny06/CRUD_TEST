from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=30,null=True, blank=True)
    password = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
