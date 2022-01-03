from django import forms
from .models import StudentInfo, StudentSem,StudentSubjectInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'batch_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date'}),
            'usn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
        
            
        }

class CreateSubject(forms.ModelForm):
    class Meta:
        model = StudentSubjectInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'batch_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date'}),
            'usn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
        
            
        }


class CreateSem(forms.ModelForm):
    class Meta:
        model = StudentSem
        exclude = ("student_img", "fathers_img", "mothers_img", )
        widgets = {
            'batch_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Academic Year'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Admission Date'}),
            'usn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'section_type': forms.Select(attrs={'class': 'form-control'}),
        
            
        }

