# Generated by Django 3.2.8 on 2022-01-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_rename_sem_name_studentsubjectinfo_sem_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='student_img',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
