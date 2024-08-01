from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    pass



class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    list_content = models.CharField(max_length=999)
    date_created = models.DateTimeField(timezone.now())

    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date_created.strftime('%Y-%m-%d')}"