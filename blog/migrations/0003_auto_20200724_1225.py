# Generated by Django 2.2.14 on 2020-07-24 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200724_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titles',
            new_name='title',
        ),
    ]