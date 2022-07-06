from django.db import models

# Create your models here.

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

"""


class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    other = models.CharField(max_length=200)


class Job(models.Model):
    name = models.CharField(max_length=100)
    other = models.CharField(max_length=200)


def __str__(self):
    return '<human:id='+str(self.id)+self.name+str(self.age)
