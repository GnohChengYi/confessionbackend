# Generated by Django 3.0.7 on 2020-12-06 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('time_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
