# Generated by Django 2.2.14 on 2020-08-03 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.TextField(default='https://i.kym-cdn.com/photos/images/facebook/001/430/011/c1d.png'),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('Hobby', 'Hobby'), ('Projects', 'Projects')], default='Hobby', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]