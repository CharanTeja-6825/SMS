from django import forms
from .models import Task, AddCourse, Marks


class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content']


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']