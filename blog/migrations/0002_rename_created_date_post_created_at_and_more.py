# Generated by Django 4.2.16 on 2024-11-08 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='published_at',
        ),
    ]