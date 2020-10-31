# Generated by Django 3.1.1 on 2020-10-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='anemia',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='covid',
            field=models.CharField(default='yes', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='days',
            field=models.CharField(default='14', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='doctors_prescription',
            field=models.CharField(default='yes', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='infectious_diseases',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='pregnant',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.CharField(default='yes', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='weight',
            field=models.IntegerField(default=60),
        ),
    ]
