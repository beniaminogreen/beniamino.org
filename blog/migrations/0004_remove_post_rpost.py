# Generated by Django 2.1.7 on 2019-04-29 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_rpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Rpost',
        ),
    ]
