from django.db import models
from adminapp.models import StudentList

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

  # Importing the StudentList model


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('LAA', 'Linux Administration and Automation'),
    ]
    SECTION_CHOICES = [
        ('S11', 'Section S11'),
        ('S12', 'Section S12'),
        ('S13', 'Section S13'),
        ('S14', 'Section S14'),
        ('S15', 'Section S15'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def str(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'


class Marks(models.Model):
    COURSE_CHOICES=[
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('OS', 'Operating Systems'),
        ('AIML', 'Artificial Intelligence and Machine Learning'),
        ('LINUX', 'Linux Administration and Automation'),
        ('FR', 'French Language')
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50,choices=COURSE_CHOICES)
    marks = models.IntegerField()
    def str(self):
        return f"{self.student.name}-{self.course}"
