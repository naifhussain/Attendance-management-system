from django.urls import path
from . import views

urlpatterns = [
    path('allstudents/', views.student_list, name='student_list'),
    path('<int:student_id>/', views.single_student, name='single_student'),
    path('registration/', views.student_regi, name='student_regi'),
    path('edit/<int:pk>', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>', views.delete_student, name='delete_student'),
    path('attendance/count/', views.attendance_count, name='attendance_count'),
    path('attendance/<student_id>',views.increase_att,name='increase_att'),
    path('subject/registration/', views.create_subject, name='create_subject'),
    path('allsubject/', views.subject_list, name='subject_list'),
    path('<slug:subject_code>/', views.single_subject, name='single_subject'),
    path('edit/<slug:pk>', views.edit_subject, name='edit_subject'),
    path('delete/<slug:subject_code>', views.delete_subject, name='delete_subject'),
]

