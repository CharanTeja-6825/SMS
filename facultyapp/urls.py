from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'facultyapp'

urlpatterns = [
    path('faculty_homepage/', views.faculty_homepage, name='faculty_homepage'),
    path('view_student_list/', views.view_student_list, name='view_student_list'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<int:pk>/delete/', views.delete_task, name='delete'),
    path('add_course/', views.add_course, name='add_course'),
    path('post_marks/', views.post_marks, name='post_marks'),
]
