from django.db import models
from django.db.models.deletion import CASCADE
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
    branch_short_name = models.CharField(max_length=3)

    def __str__(self):
        return self.branch_short_name

class ClassName(models.Model):
    batch_year=models.ForeignKey(StudentBatch,on_delete=CASCADE)
    branch_name =models.ForeignKey(StudentBranch,on_delete=CASCADE)
    section_name = models.ForeignKey(StudentSectionInfo,on_delete=CASCADE)
    # class_code= section_name+str(batch_year)+branch_name
    
    def __str__(self):
        return self.branch_name

class StudentSubjectInfo(models.Model):
    subject_name = models.CharField(max_length=30) #new
    subject_code = models.CharField(max_length=10,primary_key=True) #new
    professor_name = models.ForeignKey(TeacherInfo,on_delete=CASCADE)
    # section_name = models.ForeignKey(StudentSectionInfo,on_delete=CASCADE)
    # branch_name = models.ForeignKey(StudentBranch,on_delete=CASCADE)
    # batch_year = models.ForeignKey(StudentBatch,on_delete=CASCADE)

    def __str__(self):
        return self.subject_name





class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=100)

    def __str__(self):
        return self.shift_name



class StudentInfo(models.Model):
    batch_year = models.ForeignKey(StudentBatch,max_length=4,on_delete=CASCADE)
    admission_date = models.DateField()
    usn = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    subject_name = models.ForeignKey(StudentSubjectInfo, on_delete=models.CASCADE)
    section_type = models.ForeignKey(StudentSectionInfo, on_delete=models.CASCADE)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    student_img = models.ImageField(upload_to='photos/%Y/%m/%d/')

    sub1 = models.ForeignKey(StudentSubjectInfo, on_delete=models.CASCADE,related_name='sub1')
    sub1_attendance = models.IntegerField()
    sub2 = models.ForeignKey(StudentSubjectInfo, on_delete=models.CASCADE,related_name='sub2')
    sub2_attendance = models.IntegerField()

    sub3 = models.ForeignKey(StudentSubjectInfo, on_delete=models.CASCADE,related_name='sub3')
    sub3_attendance = models.IntegerField()
    sub4 = models.ForeignKey(StudentSubjectInfo, on_delete=models.CASCADE,related_name='sub4')
    sub4_attendance = models.IntegerField()

    sub5 = models.ForeignKey(StudentSubjectInfo, on_delete=models.CASCADE,related_name='sub5')
    sub5_attendance = models.IntegerField()
    sub6 = models.ForeignKey(StudentSubjectInfo, on_delete=models.CASCADE,related_name='sub6')
    sub6_attendance = models.IntegerField()   

    class Meta:
        unique_together = ["usn", "subject_name"]

    def __str__(self):
        return self.name


class AttendanceManager(models.Manager):
    def create_attendance(self, student_class, student_id):
        student_obj = StudentInfo.objects.get(
            class_type__class_short_form=student_class,
            admission_id=student_id
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
        return self.student.admission_id

        # # for integer field
        # return str(self.student.mothers_nid)
