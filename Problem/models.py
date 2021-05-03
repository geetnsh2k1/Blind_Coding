from django.db import models

# Create your models here.
class Problem(models.Model):
    
    Name = models.CharField(max_length=100, blank=False)
    
    Statement = models.TextField(blank=False)
    
    def __str__(self):
        return self.Name