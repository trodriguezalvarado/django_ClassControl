# Generated by Django 5.0.3 on 2024-05-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassControls', '0005_careers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers',
            name='CareerName',
            field=models.CharField(help_text='Add a career name', max_length=100, verbose_name='Career Name'),
        ),
    ]
