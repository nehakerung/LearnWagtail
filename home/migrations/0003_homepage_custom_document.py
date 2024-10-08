# Generated by Django 4.2.16 on 2024-10-08 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
        ('home', '0002_homepage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='custom_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='documents.customdocument'),
        ),
    ]
