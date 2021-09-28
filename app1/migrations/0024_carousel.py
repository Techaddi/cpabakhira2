# Generated by Django 3.2.3 on 2021-09-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_academy_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(null=True, upload_to='assets')),
                ('Img_title', models.CharField(max_length=100, null=True)),
                ('Img_desc', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]