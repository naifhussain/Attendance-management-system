from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import CreateStudent,CreateSubject
import datetime
from django.db.models import F
from django.urls import resolve


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


def delete_student(request, student_id):
    student_delete = StudentInfo.objects.get(id=student_id)
    student_delete.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect("student_list")


def attendance_count(request):
    subject = request.GET.get("subject", None)
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
            context = {"student_list_sub1": student_list_sub1}
        elif student_list_sub2:
            context = {"student_list_sub2": student_list_sub2}
        elif student_list_sub3:
            context = {"student_list_sub3": student_list_sub3}
        elif student_list_sub4:
            context = {"student_list_sub4": student_list_sub4}
        elif student_list_sub5:
            context = {"student_list_sub5": student_list_sub5}
        elif student_list_sub6:
            context = {"student_list_sub6": student_list_sub6}
        elif student_list_lab1:
            context = {"student_list_lab1": student_list_lab1}
        elif student_list_lab2:
            context = {"student_list_lab2": student_list_lab2}
    else:
        context = {}
    return render(request, "students/attendance_count.html", context)

#cancel class views
def cancel_sub1_att(request,sub):
    s = StudentInfo.objects.filter(sub1__subject_name=sub).update(sub1_att=F('sub1_att')+1)
    student_list_sub1 = StudentInfo.objects.filter(sub1__subject_name=sub)
    context={'student_list_sub1':student_list_sub1}
    return render(request,'students/attendance_list.html',context)

def cancel_sub2_att(request,sub):
    s = StudentInfo.objects.filter(sub2__subject_name=sub).update(sub2_att=F('sub2_att')+1)
    student_list_sub2 = StudentInfo.objects.filter(sub2__subject_name=sub)
    context={'student_list_sub2':student_list_sub2}
    return render(request,'students/attendance_list.html',context)

def cancel_sub3_att(request,sub):
    s = StudentInfo.objects.filter(sub3__subject_name=sub).update(sub3_att=F('sub3_att')+1)
    student_list_sub3 = StudentInfo.objects.filter(sub3__subject_name=sub)
    context={'student_list_sub3':student_list_sub3}
    return render(request,'students/attendance_list.html',context)

def cancel_sub4_att(request,sub):
    s = StudentInfo.objects.filter(sub4__subject_name=sub).update(sub4_att=F('sub4_att')+1)
    student_list_sub4 = StudentInfo.objects.filter(sub4__subject_name=sub)
    context={'student_list_sub4':student_list_sub4}
    return render(request,'students/attendance_list.html',context)

def cancel_sub5_att(request,sub):
    s = StudentInfo.objects.filter(sub5__subject_name=sub).update(sub5_att=F('sub5_att')+1)
    student_list_sub5 = StudentInfo.objects.filter(sub5__subject_name=sub)
    context={'student_list_sub5':student_list_sub5}
    return render(request,'students/attendance_list.html',context)

def cancel_sub6_att(request,sub):
    s = StudentInfo.objects.filter(sub6__subject_name=sub).update(sub6_att=F('sub6_att')+1)
    student_list_sub6 = StudentInfo.objects.filter(sub6__subject_name=sub)
    context={'student_list_sub6':student_list_sub6}
    return render(request,'students/attendance_list.html',context)

def cancel_lab1_att(request,sub):
    s = StudentInfo.objects.filter(lab1__subject_name=sub).update(lab1_att=F('lab1_att')+1)
    student_list_lab1 = StudentInfo.objects.filter(lab1__subject_name=sub)
    context={'student_list_lab1':student_list_lab1}
    return render(request,'students/attendance_list.html',context)

def cancel_lab2_att(request,sub):
    s = StudentInfo.objects.filter(lab2__subject_name=sub).update(lab2_att=F('lab2_att')+1)
    student_list_lab2 = StudentInfo.objects.filter(lab2__subject_name=sub)
    context={'student_list_lab2':student_list_lab2}
    return render(request,'students/attendance_list.html',context)



#increase attendance views
def increase_sub1_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub1_att = F('sub1_att')+1
    t.save()
    student_list_sub1 = StudentInfo.objects.filter(sub1__subject_name=t.sub1)
    context={'student_list_sub1':student_list_sub1}
    return render(request,'students/attendance_list.html',context)

def increase_sub2_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub2_att = F('sub2_att')+1
    t.save()
    student_list_sub2 = StudentInfo.objects.filter(sub2__subject_name=t.sub2)
    context={'student_list_sub2':student_list_sub2}
    return render(request,'students/attendance_list.html',context)

def increase_sub3_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub3_att = F('sub3_att')+1
    t.save()
    student_list_sub3 = StudentInfo.objects.filter(sub3__subject_name=t.sub3)
    context={'student_list_sub3':student_list_sub3}
    return render(request,'students/attendance_list.html',context)

def increase_sub4_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub4_att = F('sub4_att')+1
    t.save()
    student_list_sub4 = StudentInfo.objects.filter(sub4__subject_name=t.sub4)
    context={'student_list_sub4':student_list_sub4}
    return render(request,'students/attendance_list.html',context)

def increase_sub5_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub5_att = F('sub5_att')+1
    t.save()
    student_list_sub5 = StudentInfo.objects.filter(sub5__subject_name=t.sub5)
    context={'student_list_sub5':student_list_sub5}
    return render(request,'students/attendance_list.html',context)

def increase_sub6_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.sub6_att = F('sub6_att')+1
    t.save()
    student_list_sub6 = StudentInfo.objects.filter(sub6__subject_name=t.sub6)
    context={'student_list_sub6':student_list_sub6}
    return render(request,'students/attendance_list.html',context)

def increase_lab1_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.lab1_att = F('lab1_att')+1
    t.save()
    student_list_lab1 = StudentInfo.objects.filter(lab1__subject_name=t.lab1)
    context={'student_list_lab1':student_list_lab1}
    return render(request,'students/attendance_list.html',context)

def increase_lab2_att(request,student_id):
    t = StudentInfo.objects.get(id=student_id)
    t.lab2_att = F('lab2_att')+1
    t.save()
    student_list_lab2 = StudentInfo.objects.filter(lab2__subject_name=t.lab2)
    context={'student_list_lab2':student_list_lab2}
    return render(request,'students/attendance_list.html',context)






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

def subject_list(request):
    subjects = StudentSubjectInfo.objects.all()
    paginator = Paginator(subjects, 60)
    page = request.GET.get('page')
    paged_subjects = paginator.get_page(page)

    context = {
        "subjects": paged_subjects
    }
    return render(request, "subjects/subject_list.html", context)

def single_subject(request, subject_code):
    single_subject = get_object_or_404(StudentSubjectInfo, pk=subject_code)
    context = {
        "single_subject": single_subject
    }
    return render(request, "subjects/single_subject.html", context)

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

def delete_subject(request, subject_code):
    subject_delete = StudentSubjectInfo.objects.get(subject_code=subject_code)
    subject_delete.delete()
    messages.success(request, "Deleted Subject Info Successfully")
    return redirect("subject_list")