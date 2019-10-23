from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SurveyForm(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    initialday = models.DateTimeField(auto_now=True)
    lastmodified = models.DateTimeField(auto_now=True)
    starttimeevaluation = models.datetime()
    endtimeevaluation = models.datetime()
    
    def __str__ (self):
        return self.title