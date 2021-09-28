# Generated by Django 3.2.3 on 2021-09-10 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_news_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='assets'),
            preserve_default=False,
        ),
    ]
