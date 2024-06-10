from django.db import models
from Auth_App.models import CustomUser
# Create your models here.

taskstatus = (
    ('complete', 'Complete Task'),
    ('ongoing', 'Ongoing Task'),
    ('pending', 'Not Started')


)
taskimportant = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('hot', 'Hot')


)


class Task(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=20)
    task_description = models.CharField(max_length=50)
    assignTaskDate = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    important = models.CharField(choices=taskimportant, max_length=25, default="low")
    task_status = models.CharField(choices=taskstatus, max_length=25, default="pending")
    def __str__(self) -> str:
        return self.task_name