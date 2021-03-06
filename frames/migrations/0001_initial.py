# Generated by Django 3.1 on 2020-08-30 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeepSet',
            fields=[
                ('painting_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('integer', models.IntegerField(blank=True, null=True)),
                ('artist', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Floating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('integer', models.IntegerField(blank=True, null=True)),
                ('artist', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('integer', models.IntegerField(blank=True, null=True)),
                ('artist', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Modern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('integer', models.IntegerField(blank=True, null=True)),
                ('artist', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TableTop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('integer', models.IntegerField(blank=True, null=True)),
                ('artist', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
