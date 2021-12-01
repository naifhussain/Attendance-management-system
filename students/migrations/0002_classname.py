# Generated by Django 3.2.8 on 2021-11-23 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentbatch')),
                ('branch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentbranch')),
                ('section_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentsectioninfo')),
            ],
        ),
    ]
