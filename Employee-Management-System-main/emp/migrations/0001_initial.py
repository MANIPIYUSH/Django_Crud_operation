# Generated by Django 4.1.4 on 2023-01-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=50)),
                ('doj', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('onleave', models.BooleanField(default=True)),
            ],
        ),
    ]
