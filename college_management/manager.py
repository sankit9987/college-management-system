from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
class CustomeUserManger(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("Email is required"))
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("super user is "))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("super user is "))
        return self.create_user(email,password,**extra_fields)

    def create_faculty(self,email,password,name,mobile_no,Gender,Address,date_of_birth,profile,Qualification,department,Salary,subject,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_faculty',True)
        extra_fields.setdefault('is_student',False)
        extra_fields.setdefault('is_accountant',False)
        extra_fields.setdefault('is_library',False)

        email = self.normalize_email(email)
        user = self.model(email = email,name=name,mobile_no=mobile_no,Gender=Gender,Address=Address,date_of_birth=date_of_birth,profile=profile,Qualification=Qualification,department=department,Salary=Salary,subject=subject,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_accountant(self,email,password,name,mobile_no,Gender,Address,date_of_birth,profile,Qualification,Salary,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_faculty',False)
        extra_fields.setdefault('is_student',False)
        extra_fields.setdefault('is_accountant',True)
        extra_fields.setdefault('is_library',False)

        email = self.normalize_email(email)
        user = self.model(email = email,name=name,mobile_no=mobile_no,Gender=Gender,Address=Address,date_of_birth=date_of_birth,profile=profile,Qualification=Qualification,Salary=Salary,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_librarian(self,email,password,name,mobile_no,Gender,Address,date_of_birth,profile,Qualification,Salary,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_faculty',False)
        extra_fields.setdefault('is_student',False)
        extra_fields.setdefault('is_accountant',False)
        extra_fields.setdefault('is_library',True)

        email = self.normalize_email(email)
        user = self.model(email = email,name=name,mobile_no=mobile_no,Gender=Gender,Address=Address,date_of_birth=date_of_birth,profile=profile,Qualification=Qualification,Salary=Salary,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_student(self,email,password,name,mobile_no,Gender,Address,date_of_birth,profile,department,year,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_faculty',False)
        extra_fields.setdefault('is_student',True)
        extra_fields.setdefault('is_accountant',False)
        extra_fields.setdefault('is_library',False)

        email = self.normalize_email(email)
        user = self.model(email = email,name=name,mobile_no=mobile_no,Gender=Gender,Address=Address,date_of_birth=date_of_birth,profile=profile,year=year,department=department,**extra_fields)
        user.set_password(password)
        user.save()
        return user