# Generated by Django 3.2.3 on 2021-09-04 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_faculties_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='img1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='assets'),
            preserve_default=False,
        ),
    ]
