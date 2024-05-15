from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Exam(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField()
  name = models.CharField(max_length=255)
  questions_attempted = models.PositiveIntegerField()
  
  def __str__(self):
    return self.name

class Subject(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class QuestionBank(models.Model):
  name = models.CharField(max_length=100)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Question(models.Model):
  topic = models.CharField(max_length=100)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  level = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  mode = models.CharField(max_length=50)
  question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)

  def __str__(self):
    return self.topic