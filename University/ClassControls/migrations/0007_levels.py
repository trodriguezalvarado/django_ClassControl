# Generated by Django 5.0.3 on 2024-05-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassControls', '0006_alter_careers_careername'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LevelName', models.CharField(help_text='Add a level name', max_length=50, verbose_name='Level Name')),
            ],
        ),
    ]
