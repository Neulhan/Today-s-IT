# Generated by Django 2.2.7 on 2019-12-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20191204_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='key_from',
            field=models.ManyToManyField(to='backend.News'),
        ),
    ]