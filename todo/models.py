from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null = True, blank = True) # manage everything to do with app
    title = models.CharField(max_length=200, null = True)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True) # auto make current time the created time

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] 