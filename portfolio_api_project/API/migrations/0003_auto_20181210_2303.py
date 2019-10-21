# Generated by Django 2.1.3 on 2018-12-10 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20181210_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='date_entered',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='investment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]