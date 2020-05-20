# Generated by Django 2.2.10 on 2020-05-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200520_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptName', models.CharField(max_length=100)),
                ('ptAge', models.IntegerField()),
                ('ptPhone', models.CharField(max_length=15)),
            ],
        ),
    ]
