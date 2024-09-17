from django.utils import timezone
from django.db import models


# Create your models here.
class Problem(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В роботі'),
        ('ready', 'Готово'),
        ('completed', 'Завершено'),
    ]

    ID = models.AutoField(primary_key=True)
    name = models.TextField()
    problem = models.TextField()
    number = models.CharField(max_length=13)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    start_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.ID) + ' ' + self.number

class ActiveProblem(models.Model):
    problem = models.ForeignKey('Problem', on_delete=models.DO_NOTHING)
    def __str__(self):
        return f'{str(self.problem.ID)} {self.problem.problem}'