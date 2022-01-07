from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from teachers.models import TeacherInfo

# Create your models here.


class StudentBatch(models.Model): #new
    batch_year = models.IntegerField(max_length=4)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.batch_year)


class StudentSectionInfo(models.Model):
    section_name = models.CharField(max_length=20)

    def __str__(self):
        return self.section_name


class StudentBranch(models.Model): #new
    branch_name = models.CharField(max_length=3)

    def __str__(self):
        return self.branch_name

class StudentSem(models.Model):
    sem_number = models.IntegerField(max_length=1,primary_key=True)
    sem_name = models.CharField(max_length=10)
    start_date = models.DateField(default='2021-08-02')
    end_date = models.DateField(default='2022-01-31')

    def __str__(self):
        return self.sem_name



class StudentSubjectInfo(models.Model):
    subject_name = models.CharField(max_length=30) #new
    subject_code = models.CharField(max_length=10,primary_key=True) #new
    professor_name = models.ForeignKey(TeacherInfo,on_delete=CASCADE,default=None, blank=True, null=True)
    branch_name = models.ForeignKey(StudentBranch,on_delete=CASCADE)
    sem_number = models.ForeignKey(StudentSem,on_delete=CASCADE,default='3')
    

    def __str__(self):
        return self.subject_name





class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=100)

    def __str__(self):
        return self.shift_name



class StudentInfo(models.Model):
    batch_year = models.ForeignKey(StudentBatch,max_length=4,on_delete=CASCADE)
    admission_date = models.DateField()
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    sem_name = models.ForeignKey(StudentSem,on_delete=CASCADE)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    section_type = models.ForeignKey(StudentSectionInfo, on_delete=models.CASCADE)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    branch_name = models.ForeignKey(StudentBranch,on_delete=CASCADE)
    student_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    sub1 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='sub1',null=True)
    sub1_att = models.IntegerField(null=True,default=0)
    sub2 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='sub2',null=True)
    sub2_att = models.IntegerField(null=True,default=0) 
    sub3 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='sub3',null=True)
    sub3_att = models.IntegerField(null=True,default=0) 
    sub4 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='sub4',null=True)
    sub4_att = models.IntegerField(null=True,default=0)
    sub5 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='sub5',null=True)
    sub5_att = models.IntegerField(null=True,default=0)
    sub6 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='sub6',null=True)
    sub6_att = models.IntegerField(null=True,default=0)

    lab1 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='lab1',null=True)
    lab1_att = models.IntegerField(null=True,default=0)
    lab2 = models.ForeignKey(StudentSubjectInfo,on_delete=SET_NULL,related_name='lab2',null=True)
    lab2_att = models.IntegerField(null=True,default=0)
    att_percent_sub1 = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    att_percent_sub2 = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    att_percent_sub3 = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    att_percent_sub4 = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    att_percent_sub5 = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    att_percent_sub6 = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    att_percent_lab1 = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    att_percent_lab2 = models.DecimalField(default=0,decimal_places=2,max_digits=5)

    extra_class_sub1 = models.IntegerField(default=0)
    extra_class_sub2 = models.IntegerField(default=0)
    extra_class_sub3 = models.IntegerField(default=0)
    extra_class_sub4 = models.IntegerField(default=0)
    extra_class_sub5 = models.IntegerField(default=0)
    extra_class_sub6 = models.IntegerField(default=0)
    extra_class_lab1 = models.IntegerField(default=0)
    extra_class_lab2 = models.IntegerField(default=0)



    class Meta:
        unique_together = ["usn"]

    def __str__(self):
        return self.name


class AttendanceManager(models.Manager):
    def create_attendance(self, student_class, student_id):
        student_obj = StudentInfo.objects.get(
            sub1=student_class,
            usn=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.usn

        # # for integer field
        # return str(self.student.mothers_nid)

