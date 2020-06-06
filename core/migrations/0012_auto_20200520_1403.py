# Generated by Django 2.2.10 on 2020-05-20 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AddField(
            model_name='patient',
            name='ptAddress',
            field=models.CharField(default='06 Hoa Nam 3', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='ptCity',
            field=models.CharField(default='Da Nang', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='ptDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='ptHostpital',
            field=models.CharField(default='Benh Vien', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='ptIdCard',
            field=models.IntegerField(default=56665656, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='ptTime',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]