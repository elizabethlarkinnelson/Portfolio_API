# Generated by Django 2.1.3 on 2018-12-10 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='paid',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='updates',
            old_name='paid',
            new_name='cost',
        ),
    ]
