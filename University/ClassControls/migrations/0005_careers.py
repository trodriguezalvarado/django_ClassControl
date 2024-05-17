# Generated by Django 5.0.3 on 2024-05-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassControls', '0004_classtypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CareerName', models.CharField(help_text='Add a career name', max_length=50, verbose_name='Career Name')),
            ],
        ),
    ]
