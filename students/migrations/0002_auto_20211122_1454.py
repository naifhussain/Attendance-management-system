# Generated by Django 3.2.8 on 2021-11-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBatch',
            fields=[
                ('batch_year', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentBranch',
            fields=[
                ('branch_short_name', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentsectioninfo',
            name='id',
        ),
        migrations.AddField(
            model_name='studentclassinfo',
            name='class_short_form',
            field=models.CharField(default='2019cse', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentclassinfo',
            name='section_name',
            field=models.ForeignKey(default='A', on_delete=django.db.models.deletion.CASCADE, to='students.studentsectioninfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentsectioninfo',
            name='section_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='studentinfo',
            unique_together={('admission_id', 'class_type')},
        ),
        migrations.AddField(
            model_name='studentclassinfo',
            name='batch_year',
            field=models.ForeignKey(default=2019, on_delete=django.db.models.deletion.CASCADE, to='students.studentbatch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentclassinfo',
            name='branch_name',
            field=models.ForeignKey(default='cse', on_delete=django.db.models.deletion.CASCADE, to='students.studentbranch'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentinfo')),
            ],
            options={
                'unique_together': {('student', 'date')},
            },
        ),
    ]
