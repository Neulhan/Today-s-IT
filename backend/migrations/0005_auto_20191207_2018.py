# Generated by Django 2.2.7 on 2019-12-07 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_keyword_key_from'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyword',
            old_name='key',
            new_name='name',
        ),
    ]
