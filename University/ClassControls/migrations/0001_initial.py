# Generated by Django 5.0.3 on 2024-05-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(help_text='Add a name for the category', max_length=50, verbose_name='Category Name')),
            ],
        ),
    ]