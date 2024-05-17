# Generated by Django 5.0.3 on 2024-05-17 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassControls', '0009_delete_evaluations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planning_control_classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassRoom', models.CharField(help_text='Typoe a classroom', max_length=100, verbose_name='Classroom')),
                ('Evaluation', models.IntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text='choose an evaluation', null=True, verbose_name='Evaluation')),
                ('RealizationDate', models.DateField(help_text='Select a date of realization', null=True, verbose_name='Realization Date')),
                ('Observations', models.TextField(help_text='Type any observation here', verbose_name='Observations')),
                ('Carrer', models.ForeignKey(help_text='Select a career', on_delete=django.db.models.deletion.CASCADE, to='ClassControls.careers', verbose_name='Career')),
                ('ClassType', models.ForeignKey(help_text='Select a class type', on_delete=django.db.models.deletion.CASCADE, to='ClassControls.classtypes', verbose_name='Class Type')),
                ('Level', models.ForeignKey(help_text='Select a level', on_delete=django.db.models.deletion.CASCADE, to='ClassControls.levels', verbose_name='Level')),
                ('Responsibble', models.ForeignKey(help_text='Select a responsible', on_delete=django.db.models.deletion.CASCADE, to='ClassControls.responsibles', verbose_name='Responsible')),
            ],
        ),
    ]
