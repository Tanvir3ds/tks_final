# Generated by Django 3.0.7 on 2020-06-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tks', '0003_auto_20200623_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='Awards')),
                ('description', models.TextField()),
            ],
        ),
    ]