# Generated by Django 2.2.7 on 2019-12-04 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='exposed_sequence',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='main_key_word',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='reference',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='written_date',
            field=models.TextField(default=''),
        ),
    ]
