# Generated by Django 5.0.7 on 2024-10-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0006_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='course',
            field=models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development'), ('OS', 'Operating Systems'), ('AIML', 'Artificial Intelligence and Machine Learning'), ('LINUX', 'Linux Administration and Automation'), ('FR', 'French Language')], max_length=50),
        ),
    ]
