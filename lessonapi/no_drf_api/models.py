from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.CharField(max_length = 255)

    def __str__(self):
        return self.user.email


class Presentation(models.Model):
    deckId = models.AutoField(primary_key = True)
    authorUsername = models.CharField(max_length = 150)
    deckSlug = models.SlugField(max_length = 150)
