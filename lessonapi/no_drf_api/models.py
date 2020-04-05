from django.db import models
# Create your models here.


class Presentation(models.Model):
    deckId = models.AutoField(primary_key=True)     
    authorUsername = models.CharField(max_length=150)
    deckSlug = models.SlugField(max_length=150)
    
