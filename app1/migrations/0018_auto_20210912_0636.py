# Generated by Django 3.2.3 on 2021-09-12 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_faculty_detail_student_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_detail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Faculty_Detail',
        ),
        migrations.DeleteModel(
            name='Student_detail',
        ),
    ]
