# Generated by Django 2.2.10 on 2020-05-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200520_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='dept',
            field=models.CharField(default='Khoa', max_length=100),
            preserve_default=False,
        ),
    ]
