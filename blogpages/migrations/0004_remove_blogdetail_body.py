# Generated by Django 4.2.16 on 2024-10-09 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpages', '0003_blogpagetags_blogdetail_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetail',
            name='body',
        ),
    ]
