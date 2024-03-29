# Generated by Django 5.0.1 on 2024-02-25 07:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg_name', models.CharField(max_length=100)),
                ('pg_address', models.CharField(max_length=500)),
                ('pg_pic', models.ImageField(default='ntr.jpg', upload_to='')),
                ('pg_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200)),
                ('profession', models.CharField(choices=[('Student', 'Student'), ('Job', 'Job')], max_length=300)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('aadhaar_card', models.FileField(upload_to='')),
                ('photo', models.ImageField(upload_to='')),
                ('pg_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.pgs')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('profile_pic', models.ImageField(upload_to='')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
