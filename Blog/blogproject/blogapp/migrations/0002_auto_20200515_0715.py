# Generated by Django 3.0.6 on 2020-05-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_data', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Lion',
        ),
    ]