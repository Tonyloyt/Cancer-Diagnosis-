# Generated by Django 3.1 on 2020-10-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elixir_app', '0004_auto_20201015_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='blood',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='cardid',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users_expert',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users_expert',
            name='username',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterModelTable(
            name='patientdetails',
            table=None,
        ),
    ]
