from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import CreateStudent,CreateSubject
import datetime
from django.db.models import F
from django.urls import resolve

#function to compute holidays
def checkGovtHoliday():
    holidayList = [
    datetime.datetime.strptime("01/01", "%d/%m"),
    datetime.datetime.strptime("13/01", "%d/%m"),
    datetime.datetime.strptime("14/01", "%d/%m"),
    datetime.datetime.strptime("20/01", "%d/%m"),
    datetime.datetime.strptime("23/01", "%d/%m"),
    datetime.datetime.strptime("26/01", "%d/%m"),
    datetime.datetime.strptime("16/02", "%d/%m"),
    datetime.datetime.strptime("19/02", "%d/%m"),
    datetime.datetime.strptime("26/02", "%d/%m"),
    datetime.datetime.strptime("27/02", "%d/%m"),
    datetime.datetime.strptime("08/03", "%d/%m"),
    datetime.datetime.strptime("11/03", "%d/%m"),
    datetime.datetime.strptime("28/03", "%d/%m"),
    datetime.datetime.strptime("29/03", "%d/%m"),
    datetime.datetime.strptime("02/04", "%d/%m"),
    datetime.datetime.strptime("04/04", "%d/%m"),
    datetime.datetime.strptime("13/04", "%d/%m"),
    datetime.datetime.strptime("14/04", "%d/%m"),
    datetime.datetime.strptime("15/04", "%d/%m"),
    datetime.datetime.strptime("21/04", "%d/%m"),
    datetime.datetime.strptime("25/04", "%d/%m"),
    datetime.datetime.strptime("07/05", "%d/%m"),
    datetime.datetime.strptime("09/05", "%d/%m"),
    datetime.datetime.strptime("14/05", "%d/%m"),
    datetime.datetime.strptime("26/05", "%d/%m"),
    datetime.datetime.strptime("12/07", "%d/%m"),
    datetime.datetime.strptime("21/07", "%d/%m"),
    datetime.datetime.strptime("15/08", "%d/%m"),
    datetime.datetime.strptime("16/08", "%d/%m"),
    datetime.datetime.strptime("19/08", "%d/%m"),
    datetime.datetime.strptime("21/08", "%d/%m"),
    datetime.datetime.strptime("22/08", "%d/%m"),
    datetime.datetime.strptime("30/08", "%d/%m"),
    datetime.datetime.strptime("10/09", "%d/%m"),
    datetime.datetime.strptime("02/10", "%d/%m"),
    datetime.datetime.strptime("12/10", "%d/%m"),
    datetime.datetime.strptime("13/10", "%d/%m"),
    datetime.datetime.strptime("14/10", "%d/%m"),
    datetime.datetime.strptime("15/10", "%d/%m"),
    datetime.datetime.strptime("19/10", "%d/%m"),
    datetime.datetime.strptime("20/10", "%d/%m"),
    datetime.datetime.strptime("24/10", "%d/%m"),
    datetime.datetime.strptime("04/11", "%d/%m"),
    datetime.datetime.strptime("05/11", "%d/%m"),
    datetime.datetime.strptime("06/11", "%d/%m"),
    datetime.datetime.strptime("10/11", "%d/%m"),
    datetime.datetime.strptime("12/11", "%d/%m"),
    datetime.datetime.strptime("19/11", "%d/%m"),
    datetime.datetime.strptime("24/11", "%d/%m"),
    datetime.datetime.strptime("24/12", "%d/%m"),
    datetime.datetime.strptime("25/12", "%d/%m"),
    ]
    nowDay=datetime.datetime.now().date().day
    nowMonth=datetime.datetime.now().date().month
    today = datetime.datetime.strptime("{}/{}".format(nowDay,nowMonth), "%d/%m")
    val = today in holidayList
    return val

def getDayName():
    now=datetime.datetime.now()
    today = now.strftime("%A")
    if today == 'Friday':
        return True
    else:
        return False

# Create your views here.
def student_list(request):
    students = StudentInfo.objects.all()
    paginator = Paginator(students, 60)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)

    context = {
        "students": paged_students
    }
    return render(request, "students/student_list.html", context)


def single_student(request, student_id):
    single_student = get_object_or_404(StudentInfo, pk=student_id)
    context = {
        "single_student": single_student
    }
    return render(request, "students/student_details.html", context)

@login_required
def student_regi(request):
    if request.method == "POST":
        forms = CreateStudent(request.POST)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Student Registration Successfully!")
        return redirect("student_list")
    else:
        forms = CreateStudent()

    context = {
        "forms": forms
    }
    return render(request, "students/registration.html", context)

@login_required
def edit_student(request, pk):
    student_edit = StudentInfo.objects.get(id=pk)
    edit_forms = CreateStudent(instance=student_edit)

    if request.method == "POST":
        edit_forms = CreateStudent(request.POST, instance=student_edit)

        if edit_forms.is_valid():
            edit_forms.save()
            messages.success(request, "Edit Student Info Successfully!")
            return redirect("student_list")

    context = {
        "edit_forms": edit_forms
    }
    return render(request, "students/edit_student.html", context)

@login_required
def delete_student(request, student_id):
    student_delete = StudentInfo.objects.get(id=student_id)
    student_delete.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect("student_list")

@login_required
def attendance_count(request):
    subject = request.GET.get("subject", None)
    subjects=StudentSubjectInfo.objects.filter(subject_name=subject)
    
    

    if subject:
        student_list_sub1 = StudentInfo.objects.filter(sub1__subject_name=subject)
        student_list_sub2 = StudentInfo.objects.filter(sub2__subject_name=subject)
        student_list_sub3 = StudentInfo.objects.filter(sub3__subject_name=subject)
        student_list_sub4 = StudentInfo.objects.filter(sub4__subject_name=subject)
        student_list_sub5 = StudentInfo.objects.filter(sub5__subject_name=subject)
        student_list_sub6 = StudentInfo.objects.filter(sub6__subject_name=subject)
        student_list_lab1 = StudentInfo.objects.filter(lab1__subject_name=subject)
        student_list_lab2 = StudentInfo.objects.filter(lab2__subject_name=subject)
        
        

        

        if student_list_sub1:
            context = {"student_list_sub1": student_list_sub1,'subjects':subjects}
        elif student_list_sub2:
            context = {"student_list_sub2": student_list_sub2,'subjects':subjects}
        elif student_list_sub3:
            context = {"student_list_sub3": student_list_sub3,'subjects':subjects}
        elif student_list_sub4:
            context = {"student_list_sub4": student_list_sub4,'subjects':subjects}
        elif student_list_sub5:
            context = {"student_list_sub5": student_list_sub5,'subjects':subjects}
        elif student_list_sub6:
            context = {"student_list_sub6": student_list_sub6,'subjects':subjects}
        elif student_list_lab1:
            context = {"student_list_lab1": student_list_lab1,'subjects':subjects}
        elif student_list_lab2:
            context = {"student_list_lab2": student_list_lab2,'subjects':subjects}
    else:
        context = {}
    if checkGovtHoliday()==True:
        now = datetime.datetime.now().date()
        messages.info(request, 'Attendance Not required, Government Holiday! '+str(now)+'.')
        return render(request,'students/attendance_count.html',context)
    elif getDayName()==True:
        messages.info(request, 'Attendance Not required, It is Friday!')
        return render(request,'students/attendance_count.html',context)
    return render(request, "students/attendance_count.html", context)

#cancel class views
@login_required
def cancel_sub1_att(request,sub):
    s = StudentInfo.objects.filter(sub1__subject_name=sub).update(sub1_att=F('sub1_att')+1)
    student_list_sub1 = StudentInfo.objects.filter(sub1__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_sub1':student_list_sub1,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def cancel_sub2_att(request,sub):
    s = StudentInfo.objects.filter(sub2__subject_name=sub).update(sub2_att=F('sub2_att')+1)
    student_list_sub2 = StudentInfo.objects.filter(sub2__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_sub2':student_list_sub2,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def cancel_sub3_att(request,sub):
    s = StudentInfo.objects.filter(sub3__subject_name=sub).update(sub3_att=F('sub3_att')+1)
    student_list_sub3 = StudentInfo.objects.filter(sub3__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_sub3':student_list_sub3,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def cancel_sub4_att(request,sub):
    s = StudentInfo.objects.filter(sub4__subject_name=sub).update(sub4_att=F('sub4_att')+1)
    student_list_sub4 = StudentInfo.objects.filter(sub4__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_sub4':student_list_sub4,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def cancel_sub5_att(request,sub):
    s = StudentInfo.objects.filter(sub5__subject_name=sub).update(sub5_att=F('sub5_att')+1)
    student_list_sub5 = StudentInfo.objects.filter(sub5__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_sub5':student_list_sub5,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def cancel_sub6_att(request,sub):
    s = StudentInfo.objects.filter(sub6__subject_name=sub).update(sub6_att=F('sub6_att')+1)
    student_list_sub6 = StudentInfo.objects.filter(sub6__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_sub6':student_list_sub6,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def cancel_lab1_att(request,sub):
    s = StudentInfo.objects.filter(lab1__subject_name=sub).update(lab1_att=F('lab1_att')+1)
    student_list_lab1 = StudentInfo.objects.filter(lab1__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_lab1':student_list_lab1,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def cancel_lab2_att(request,sub):
    s = StudentInfo.objects.filter(lab2__subject_name=sub).update(lab2_att=F('lab2_att')+1)
    student_list_lab2 = StudentInfo.objects.filter(lab2__subject_name=sub)
    subject=StudentSubjectInfo.objects.filter(subject_name=sub)
    context={'student_list_lab2':student_list_lab2,'subject':subject}
    return render(request,'students/attendance_list.html',context)

#take attendace buttons functinality
@login_required
def take_sub1_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_sub1 = StudentInfo.objects.filter(sub1__subject_name=t.sub1)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub1)
    context={'student_list_sub1':student_list_sub1,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def take_sub2_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_sub2 = StudentInfo.objects.filter(sub2__subject_name=t.sub2)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub2)
    context={'student_list_sub2':student_list_sub2,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def take_sub3_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_sub3 = StudentInfo.objects.filter(sub3__subject_name=t.sub3)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub3)
    context={'student_list_sub3':student_list_sub3,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def take_sub4_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_sub4 = StudentInfo.objects.filter(sub4__subject_name=t.sub4)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub4)
    context={'student_list_sub4':student_list_sub4,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def take_sub5_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_sub5 = StudentInfo.objects.filter(sub5__subject_name=t.sub5)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub5)

    context={'student_list_sub5':student_list_sub5,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def take_sub6_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_sub6 = StudentInfo.objects.filter(sub6__subject_name=t.sub6)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub6)
    context={'student_list_sub6':student_list_sub6,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def take_lab1_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_lab1 = StudentInfo.objects.filter(lab1__subject_name=t.lab1)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.lab1)
    context={'student_list_lab1':student_list_lab1,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def take_lab2_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    student_list_lab2 = StudentInfo.objects.filter(lab2__subject_name=t.lab2)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.lab2)
    context={'student_list_lab2':student_list_lab2,'subject':subject}
    return render(request,'students/attendance_list.html',context)


#increase attendance views
@login_required
def increase_sub1_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub1_att = F('sub1_att')+1
    t.save()
    student_list_sub1 = StudentInfo.objects.filter(sub1__subject_name=t.sub1)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub1)
    context={'student_list_sub1':student_list_sub1,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def increase_sub2_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub2_att = F('sub2_att')+1
    t.save()
    student_list_sub2 = StudentInfo.objects.filter(sub2__subject_name=t.sub2)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub2)
    context={'student_list_sub2':student_list_sub2,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def increase_sub3_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub3_att = F('sub3_att')+1
    t.save()
    student_list_sub3 = StudentInfo.objects.filter(sub3__subject_name=t.sub3)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub3)
    context={'student_list_sub3':student_list_sub3,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def increase_sub4_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub4_att = F('sub4_att')+1
    t.save()
    student_list_sub4 = StudentInfo.objects.filter(sub4__subject_name=t.sub4)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub4)
    context={'student_list_sub4':student_list_sub4,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def increase_sub5_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub5_att = F('sub5_att')+1
    t.save()
    student_list_sub5 = StudentInfo.objects.filter(sub5__subject_name=t.sub5)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub5)
    context={'student_list_sub5':student_list_sub5,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def increase_sub6_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub6_att = F('sub6_att')+1
    t.save()
    student_list_sub6 = StudentInfo.objects.filter(sub6__subject_name=t.sub6)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.sub6)

    context={'student_list_sub6':student_list_sub6,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def increase_lab1_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.lab1_att = F('lab1_att')+1
    t.save()
    student_list_lab1 = StudentInfo.objects.filter(lab1__subject_name=t.lab1)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.lab1)

    context={'student_list_lab1':student_list_lab1,'subject':subject}
    return render(request,'students/attendance_list.html',context)

@login_required
def increase_lab2_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.lab2_att = F('lab2_att')+1
    t.save()
    student_list_lab2 = StudentInfo.objects.filter(lab2__subject_name=t.lab2)
    subject=StudentSubjectInfo.objects.filter(subject_name=t.lab2)

    context={'student_list_lab2':student_list_lab2,'subject':subject}
    return render(request,'students/attendance_list.html',context)





@login_required
def create_subject(request):
    if request.method == "POST":
        forms = CreateSubject(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Subject Added Successfully!")
        return redirect("subject_list") #create list
    else:
        forms = CreateSubject()

    context = {
        "forms": forms
    }
    return render(request, "subjects/create_subject.html", context)

@login_required
def subject_list(request):
    subjects = StudentSubjectInfo.objects.all()
    paginator = Paginator(subjects, 60)
    page = request.GET.get('page')
    paged_subjects = paginator.get_page(page)

    context = {
        "subjects": paged_subjects
    }
    return render(request, "subjects/subject_list.html", context)

@login_required
def single_subject(request, subject_code):
    single_subject = get_object_or_404(StudentSubjectInfo, pk=subject_code)
    context = {
        "single_subject": single_subject
    }
    return render(request, "subjects/single_subject.html", context)

@login_required
def edit_subject(request, pk):
    subject_edit = StudentSubjectInfo.objects.get(subject_code=pk)
    edit_forms = CreateSubject(instance=subject_edit)

    if request.method == "POST":
        edit_forms = CreateSubject(request.POST, instance=subject_edit)

        if edit_forms.is_valid():
            edit_forms.save()
            messages.success(request, "Subject Info updated Successfully!")
            return redirect("subject_list")

    context = {
        "edit_forms": edit_forms
    }
    return render(request, "subjects/edit_subject.html", context)

@login_required
def delete_subject(request, subject_code):
    subject_delete = StudentSubjectInfo.objects.get(subject_code=subject_code)
    subject_delete.delete()
    messages.success(request, "Deleted Subject Info Successfully")
    return redirect("subject_list")