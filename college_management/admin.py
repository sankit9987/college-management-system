from django.contrib import admin
from .models import CustomeUser,Faculty,Department,Subject,Notification,Add_Book,Assign_book,Marks,Year,Attendance,Student
# Register your models here.
admin.site.register(CustomeUser)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Notification)
admin.site.register(Add_Book)
admin.site.register(Assign_book)
admin.site.register(Attendance)
admin.site.register(Marks)
admin.site.register(Year)
admin.site.register(Student)