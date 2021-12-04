from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField



# Create your models here.
class TeacherDeptInfo(models.Model):
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name

class TeacherInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    teacher_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    joining_date = models.DateField(null=True)
    dept_type = models.ForeignKey(TeacherDeptInfo, on_delete=models.CASCADE)
    sub1=models.ForeignKey('students.StudentSubjectInfo',on_delete=CASCADE,related_name='psub1',null=True,blank=True)
    sub2=models.ForeignKey('students.StudentSubjectInfo',on_delete=CASCADE,related_name='psub2',null=True,blank=True)
    sub3=models.ForeignKey('students.StudentSubjectInfo',on_delete=CASCADE,related_name='psub3',null=True,blank=True)
    def __str__(self):
        return self.name

