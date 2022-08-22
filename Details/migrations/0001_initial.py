# Generated by Django 4.1 on 2022-08-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=255)),
                ('numofcourse', models.IntegerField()),
                ('numofteacher', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('dateofbirth', models.DateField()),
                ('rollno', models.IntegerField()),
                ('deptname', models.CharField(max_length=100)),
                ('coursename', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
            ],
        ),
    ]