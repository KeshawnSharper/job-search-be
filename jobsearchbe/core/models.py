from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True)

    # class Meta:
    #     ordering = ('created',)

    def __str__(self):
        return self.email
