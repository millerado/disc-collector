# Generated by Django 4.1.2 on 2022-10-11 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_throws'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='throws',
            options={'ordering': ('-distance',)},
        ),
    ]
