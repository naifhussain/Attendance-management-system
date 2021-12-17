from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import CreateStudent

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

