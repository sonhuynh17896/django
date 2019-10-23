from django.db import models
from questions.models import Question
# Create your models here.

class Choice(models.Model):
    choices_text = models.CharField(max_length=150)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)

    def __str__(self):
        return self.choices_text