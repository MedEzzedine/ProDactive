# Generated by Django 3.2.9 on 2021-12-12 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('grade', models.IntegerField(default=1)),
                ('monthlyScore', models.IntegerField(default=30)),
                ('yearlyScore', models.IntegerField(default=365)),
                ('inscriptionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('WARNING', 'Warning'), ('PROMOTION', 'Promotion'), ('FIRED', 'Fired')], default='WARNING', max_length=9)),
                ('content', models.TextField()),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('employeeFK', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('justification', models.ImageField(blank=True, default='', null=True, upload_to='pdf')),
                ('valid', models.BooleanField(default=False)),
                ('checked', models.BooleanField(default=False)),
                ('employeeFK', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.employee')),
            ],
        ),
    ]
