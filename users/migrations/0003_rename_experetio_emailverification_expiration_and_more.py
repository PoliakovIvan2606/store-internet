# Generated by Django 4.2.3 on 2023-07-18 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_verifid_email_emailverification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailverification',
            old_name='experetio',
            new_name='expiration',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_verifid_email',
            new_name='is_verified_email',
        ),
    ]
