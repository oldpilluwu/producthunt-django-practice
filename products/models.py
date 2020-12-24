from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.
class Product(models.Model):
    title = CharField(max_length=255)
    pub_date = models.DateField()
    body = models.TextField()
    url = models.TextField(default='www.google.com')
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    