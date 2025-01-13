from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_id = models.CharField(max_length=100, default='N/A')  # Providing a default value

    class Meta:
        db_table = "user_student"
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ['-id']

    def __str__(self):
        return self.user.username  # or any other relevant field
