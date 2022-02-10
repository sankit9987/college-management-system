from django.db import models
from django.contrib.auth.models import User,AbstractUser,PermissionsMixin
from django.db.models.deletion import DO_NOTHING
from .manager import CustomeUserManger
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Department(models.Model):
    Department_name = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Department_name
        
class Year(models.Model):
    name =models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="depatment")
    year = models.ForeignKey(Year, on_delete=models.CASCADE,related_name="year",null=True)
    subject_name = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject_name




# class Subject(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     subject_name = models.CharField(max_length=10)
#     created_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.subject_name
Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
class CustomeUser(AbstractUser):
    username = None
    email = models.EmailField('emial address' , unique=True)
    password = models.CharField(max_length=16666)
    name= models.CharField(max_length=100)
    Gender= models.CharField(max_length=100,choices=Gender)
    Address= models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True,)
    profile = models.ImageField(upload_to='Profile', max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_library = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomeUserManger()

    def __str__(self):
        return self.email


class Faculty(CustomeUser):
    Qualification = models.CharField(max_length=20)
    Salary = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    objects = CustomeUserManger()


class Student(CustomeUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="department")
    year = models.ForeignKey(Year, on_delete=models.CASCADE,related_name="YEAR")
    created_on = models.DateTimeField(auto_now=True)

    objects = CustomeUserManger()


class Accountant(CustomeUser):
    Qualification = models.CharField(max_length=20)
    Salary = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now=True)
    
    objects = CustomeUserManger()

class Librarian(CustomeUser):
    Qualification = models.CharField(max_length=20)
    Salary = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now=True)
    
    objects = CustomeUserManger()

Status = (
    ("Present", "Present"),
    ("Absent", "Absent"),
)

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=Status)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    attendance_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)


# class AttendanceReport(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

Whome = (
    ("All", "All"),
    ("Faculty", "Faculty"),
    ("Student", "Student"),
    ("Accountant", "Accountant"),
    ("Librarian", "Librarian"),
)

class Notification(models.Model):
    id= models.AutoField(primary_key=True) 
    by = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    whome = models.CharField(max_length=10,choices=Whome)
    message = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.whome

class Add_Book(models.Model):
    id = models.AutoField(primary_key=True)
    Book_name = models.CharField(max_length=100)
    publication = models.CharField(max_length=20)
    quantity = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Book_name
    


class Assign_book(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Add_Book, on_delete=models.CASCADE)
    assign_date = models.DateField()
    due_date = models.DateField()
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    add_mark = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)