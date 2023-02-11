# Generated by Django 4.1.6 on 2023-02-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=200)),
                ('Issue', models.TextField()),
            ],
        ),
    ]