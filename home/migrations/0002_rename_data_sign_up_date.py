# Generated by Django 5.1.1 on 2024-10-14 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sign_up',
            old_name='data',
            new_name='date',
        ),
    ]
