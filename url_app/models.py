from django.db import models
from django.contrib.auth.models import User

class ShortenURL(models.Model):
    original_url = models.URLField()
    short_key = models.CharField(max_length=10, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    
    def __str__(self):
        return self.short_key