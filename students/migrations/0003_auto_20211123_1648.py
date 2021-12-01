# Generated by Django 3.2.8 on 2021-11-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_classname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='class_type',
            new_name='subject_name',
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='usn',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='studentinfo',
            unique_together={('usn', 'subject_name')},
        ),
    ]
