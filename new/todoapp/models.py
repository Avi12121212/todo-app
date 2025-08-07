from django.db import models


from django.db import models

class UserProfile(models.Model):
    yourname = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    father_name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f" {self.yourname,self.mobile_number,self.father_name,self.email_id,self.password}"
    # self.yourname,self.father_name


# Create your models here.
