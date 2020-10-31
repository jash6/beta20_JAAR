# Generated by Django 3.1.1 on 2020-10-31 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donordetails',
            name='anemia',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='covid',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='days',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='doctors_prescription',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='infectious_diseases',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='pregnant',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='donordetails',
            name='test',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Hospital',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='blood_group',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='has_corona',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_donor',
            field=models.BooleanField(default=''),
        ),
    ]
