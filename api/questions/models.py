from django.db import models
from django.contrib.auth.models import User
from surveyforms.models import SurveyForm
from choices.models import Choice
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    id_form = models.ForeignKey(SurveyForm, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
