from typing import ValuesView
from django.urls import path
from django.contrib.auth.views import PasswordResetView,SetPasswordForm
from django.contrib.auth import views as auth_views
from .form import Password_reset,Password_confirm
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path("logout",views.user_logout,name="logout"),

    path("password-reset",auth_views.PasswordResetView.as_view(template_name="password-reset.html",form_class=Password_reset),name="password_reset"),


    path("password-reset/Done",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_Confirm.html",form_class=Password_confirm), name="password_reset_confirm"),


    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_Complete.html"),name="password_reset_complete"),
    
    path("Edit",views.edit,name="edit"),
    path("Notification",views.notification,name="Notification"),

    path('Dashboard',views.Hod_dashboard,name="Hod_dashboard"),
    path('add_fuculty',views.add_faculty,name="add_faculty"),
    path('View_faculty',views.View_faclty,name="View_faculty"),
    path('Delete_faculty/<int:id>',views.Delete_faclty,name="Delete_faclty"),
    path('Faculty/<str:email>',views.faculty,name="Faculty"),

    path('Add_accountant',views.add_accountant,name="add_accountant"),
    path('View_accountant',views.View_accountant,name="View_accountant"),
    path('Delete_accountant/<int:id>',views.Delete_accountant,name="Delete_accountant"),
    path('Accountant/<str:email>',views.accountant,name="accountant"),

    path('Add_librarian',views.add_librarian,name="add_librarian"),
    path('View_librarian',views.View_librarian,name="View_librarian"),
    path('Delete_librarian/<int:id>',views.Delete_librarian,name="Delete_librarian"),
    path('Librarian/<str:email>',views.librarian,name="librarian"),

    path('Accountant_Dashboard',views.accountant_Dashboard,name="accountant_Dashboard"),
    path('Add_student',views.add_student,name="add_student"),
    path('View_student',views.view_student,name="view_student"),
    path('Delete_student/<int:id>',views.Delete_student,name="Delete_student"),
    path('student/<str:email>',views.student,name="student"),
    path("edit",views.edit_accountant,name="edit_accountant"),

    path('Librarian_Dashboard',views.librarian_Dashboard,name="librarian_Dashboard"),
    path('Assign_Book',views.Assign_Book,name="Assign_Book"),
    path('view_assign_Book',views.view_assig_Book,name="view_assig_Book"),
    path('view-assign-Book/<int:id>',views.view_assign_book_details,name="view_assign_book_details"),
    path('Book',views.Book,name="Book"),
    path('Add-Book',views.add_book,name="Add_book"),

    path('Student_Dashboard',views.Student_Dashboard,name="Student_Dashboard"),
    path("edit-profile",views.edit_student,name="edit_student"),
    path("attendance",views.attendance,name="attendance"),


    path("Add_marks",views.Add_marks,name="Add_marks"),
    path("Add-attendance",views.Add_attendance,name="Add_attendance"),

    path("Faculty_Dashboard",views.Faculty_Dashboard,name="Faculty_Dashboard"),
    path("Save_marks",views.Save_marks,name="Save_marks"),
    path("save_attendance",views.save_attendance,name="save_attendance"),
]
