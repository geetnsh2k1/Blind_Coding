from django.db import models
from django.contrib.auth.models import User as Usr
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
    
    Created = models.DateTimeField(auto_now_add=True)
    
    User = models.OneToOneField(Usr, unique=True, on_delete=models.CASCADE, null=False)
    
    Phone = models.IntegerField(validators=[RegexValidator("[1-9]{1}[0-9]{9}", "Enter the phone number without 0 and country code.", "Enter the phone number without 0 and country code.")], null=False)
        
    College = models.CharField(max_length=200, blank=True)
    
    Code = models.TextField(blank=True)
    
    def __str__(self):
        return self.User.username