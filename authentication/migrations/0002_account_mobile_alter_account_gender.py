# Generated by Django 4.0.5 on 2022-06-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='mobile',
            field=models.CharField(default=10000, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=6),
        ),
    ]
