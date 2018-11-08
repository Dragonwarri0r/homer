# Generated by Django 2.1.1 on 2018-10-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodeid', models.IntegerField()),
                ('nodename', models.CharField(max_length=8)),
                ('nodestatus', models.BooleanField()),
                ('nodetime', models.DateTimeField()),
            ],
        ),
    ]
