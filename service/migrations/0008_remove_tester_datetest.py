# Generated by Django 2.1.2 on 2018-11-25 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_tester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tester',
            name='dateTest',
        ),
    ]
