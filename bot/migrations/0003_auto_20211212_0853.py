# Generated by Django 3.2.9 on 2021-12-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_absence_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='absence',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='yearlyScore',
            field=models.IntegerField(default=365),
        ),
    ]
