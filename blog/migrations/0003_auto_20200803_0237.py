# Generated by Django 2.2.14 on 2020-08-03 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200803_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('Hobby', 'Hobby'), ('Projects', 'Projects')], default='Hobby', max_length=8),
        ),
    ]