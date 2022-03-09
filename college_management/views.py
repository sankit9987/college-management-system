from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Faculty,Department,Subject,Accountant,Librarian,CustomeUser,Notification,Student,Add_Book,Assign_book,Year,Marks,Attendance,CustomeUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response  import JsonResponse
from django.http import HttpResponse
import os
from datetime import date
from .form import Password_confirm
from datetime import date

# Login 
def index(request):
    print(Password_confirm)
    if not request.user.is_authenticated:
        if request.method=='POST':
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(email = username,password=password)
            if user:
                login(request, user)
                messages.success(request,"Login Successfully!!!") 
                if request.user.is_faculty:
                    return redirect("Faculty_Dashboard")
                elif request.user.is_superuser:
                    return redirect("Hod_dashboard")
                elif request.user.is_accountant:
                    return redirect("accountant_Dashboard")
                elif request.user.is_library:
                    return redirect("librarian_Dashboard")
                else:
                    return redirect("Student_Dashboard")
            else:
                messages.error(request,"Please check username and password!!!") 
        return render(request, 'login.html')
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")



#Edit User
@login_required(login_url='index')
def edit(request):
    if request.user.is_superuser:
        if request.method=="POST":
            user = CustomeUser.objects.get(id=request.user.id)
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            password = request.POST['password']
            l=user.set_password(password)
            user.save()
            username = request.user.email
            user=authenticate(email = username,password=password)
            if user:
                login(request, user)
            CustomeUser.objects.filter(email=request.user).update(name=name,Gender=gender,Address=address,mobile_no=mobile,date_of_birth=dob)
            messages.success(request,"Update successfully!!!") 
            return redirect("Hod_dashboard")
        return render(request,"Hod/edit_user.html")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# User Logout
@login_required(login_url='index')
def user_logout(request):
    logout(request)
    return redirect("index")
# Admin Work

#Admin Dashboard
@login_required(login_url='index')
def Hod_dashboard(request):
    if request.user.is_superuser:
        faculty = Faculty.objects.all().count()
        accountant = Accountant.objects.all().count()
        librarian = Librarian.objects.all().count()
        student = Student.objects.all().count()
        return render(request,"Hod/Hod_dashboard.html",{"faculty":faculty,"accountant":accountant,"librarian":librarian,"student":student})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def notification(request):
    if request.method=="POST":
        whom = request.POST['whom']
        message = request.POST['message']
        Notification.objects.create(by=request.user,whome=whom,message=message)
        messages.success(request, "Message send successfully")
        return redirect("Hod_dashboard")
    if request.user.is_superuser:
        return render(request,"Hod/Send_Notification.html")
    elif request.user.is_faculty:
        return render(request,"Faculty/Send_Notification.html")
    elif request.user.is_accountant:
        return render(request,"Accountant/Send_Notification.html")
    elif request.user.is_library:
        return render(request,"Librarian/Send_Notification.html")    
    else:
        return render(request,"Student/Send_Notification.html")
# Add Faculty
@login_required(login_url='index')
def add_faculty(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            email = request.POST['email']
            qualification = request.POST['qualification']
            salary = request.POST['salary']
            subject = request.POST['subject']
            profile = request.FILES['profile']
            password = request.POST['password']
            department = request.POST['department']
            depart = Department.objects.get(Department_name=department)
            sub  = Subject.objects.get(subject_name=subject)
            user = CustomeUser.objects.filter(email=email)
            if user:
                messages.error(request,"User Already exits!!!") 
                return redirect("add_faculty")
            else:
                Faculty.objects.create_faculty(email=email, password=password, name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob, profile=profile, Qualification=qualification, department=depart, Salary=salary, subject=sub)
            messages.success(request,"Add successfully!!!") 
            return redirect("View_faculty")
        department = Department.objects.all()
        subject = Subject.objects.all()
        
        return render(request,"Hod/Add_faculty.html",{"department":department,"subject":subject})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")

#View Faculty
@login_required(login_url='index')
def View_faclty(request):
    if request.user.is_superuser:
        faculty = Faculty.objects.all()
        return render(request,"Hod/View_faculty.html",{"faculty":faculty})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")

# Delete Faculty
@login_required(login_url='index')
def Delete_faclty(request,id):
    if request.user.is_superuser:
        faculty = Faculty.objects.get(id=id)
        faculty.delete()
        messages.success(request,"Delete successfully!!!") 
        return redirect("View_faculty")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")

# View Single Faculty
@login_required(login_url='index')
def faculty(request,email):
    if request.user.is_superuser:
        if request.method=="POST":
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            qualification = request.POST['qualification']
            salary = request.POST['salary']
            Faculty.objects.filter(email=email).update(name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob,  Qualification=qualification, Salary=salary)
            if request.FILES:
                profile = request.FILES['profile']
                faclty = Faculty.objects.get(email = email)
                os.remove(faclty.profile.path)
                faclty.profile = profile
                faclty.save()
            messages.success(request,"Update successfully!!!") 
            return redirect("View_faculty")
        filter = Faculty.objects.filter(email=email)
        return render(request, "Hod/View_faculty_details.html",{"faculty":filter})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# Add Accountant
@login_required(login_url='index')
def add_accountant(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            email = request.POST['email']
            qualification = request.POST['qualification']
            salary = request.POST['salary']
            profile = request.FILES['profile']
            password = request.POST['password']
            Accountant.objects.create_accountant(email=email, password=password, name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob, profile=profile, Qualification=qualification, Salary=salary)
            messages.success(request,"Accountant add successfully!!!") 
            return redirect("View_accountant")
        return render(request,"Hod/Add_accountant.html")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# View Accountant
@login_required(login_url='index')
def View_accountant(request):
    if request.user.is_superuser:
        accountant = Accountant.objects.all()
        return render(request,"Hod/View_accountant.html",{"accountant":accountant,})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# Delete Accountant
def Delete_accountant(request,id):
    if request.user.is_superuser:
        accountant = Accountant.objects.get(id=id)
        accountant.delete()
        messages.success(request,"Delete successfully!!!") 
        return redirect("View_accountant")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# Update Accountant Details
@login_required(login_url='index')
def accountant(request,email):
    if request.user.is_superuser:
        if request.method=="POST":
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            qualification = request.POST['qualification']
            salary = request.POST['salary']
            Accountant.objects.filter(email=email).update(name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob,  Qualification=qualification, Salary=salary)
            if request.FILES:
                profile = request.FILES['profile']
                faclty = Accountant.objects.get(email = email)
                os.remove(faclty.profile.path)
                faclty.profile = profile
                faclty.save()
            messages.success(request,"Update successfully!!!") 
            return redirect("View_accountant")
        filter = Accountant.objects.filter(email=email)
        return render(request, "Hod/View_accountant_details.html",{"accountant":filter,})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# Add Librarian
@login_required(login_url='index')
def add_librarian(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            email = request.POST['email']
            qualification = request.POST['qualification']
            salary = request.POST['salary']
            profile = request.FILES['profile']
            password = request.POST['password']
            l = CustomeUser.objects.filter(email=email)
            if l:
                messages.error(request,"User already exists!!!") 
                return redirect("add_librarian")
            else:
                Librarian.objects.create_librarian(email=email, password=password, name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob, profile=profile, Qualification=qualification, Salary=salary)
                messages.success(request,"Add successfully!!!") 
                return redirect("View_librarian")
        return render(request,"Hod/Add_librarian.html",{})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")

# View Librarian
@login_required(login_url='index')
def View_librarian(request):
    if request.user.is_superuser:
        librarian = Librarian.objects.all()
        return render(request,"Hod/View_librarian.html",{'librarian':librarian})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# Delete Librarian
@login_required(login_url='index')
def Delete_librarian(request,id):
    if request.user.is_superuser:
        librarian = Librarian.objects.get(id=id)
        librarian.delete()
        messages.success(request,"Delete successfully!!!") 
        return redirect("View_librarian")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
# Update Librarian Details
@login_required(login_url='index')
def librarian(request,email):
    if request.user.is_superuser:
        if request.method=="POST":
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            qualification = request.POST['qualification']
            salary = request.POST['salary']
            Librarian.objects.filter(email=email).update(name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob,  Qualification=qualification, Salary=salary)
            messages.success(request,"Update successfully!!!") 
            if request.FILES:
                profile = request.FILES['profile']
                faclty = Librarian.objects.get(email = email)
                os.remove(faclty.profile.path)
                faclty.profile = profile
                faclty.save()
            return redirect("View_librarian")
        filter = Librarian.objects.filter(email=email)
        return render(request, "Hod/View_librarian_details.html",{"librarian":filter,})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def accountant_Dashboard(request):
    if request.user.is_accountant:
        notification = Notification.objects.filter(Q(whome="Accountant") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Accountant") | Q(whome="All")).filter(status=False).count()
        return render(request,"Accountant/accountant_Dashboard.html",{"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def add_student(request):
    if request.user.is_accountant:
        if request.method == 'POST':
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            email = request.POST['email']
            year = request.POST['year']
            profile = request.FILES['profile']
            password = request.POST['password']
            department = request.POST['department']
            depart = Department.objects.get(Department_name=department)
            YEAR = Year.objects.get(name=year)
            s = CustomeUser.objects.filter(email=email)
            if s:
                messages.error(request,"User already exist!!!") 
                return redirect('add_student')
            else:
                
                Student.objects.create_student(email=email, password=password, name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob, profile=profile, year=YEAR, department=depart)
                messages.success(request,"Add successfully!!!") 
                return redirect("view_student")
        department = Department.objects.all()
        return render(request,"Accountant/Add_student.html",{'department':department})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def view_student(request):
    if request.user.is_accountant:
        student = Student.objects.all()
        return render(request,"Accountant/view_student.html",{"student":student})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def Delete_student(request,id):
    if request.user.is_accountant:
        student = Student.objects.get(id=id)
        student.delete()
        return redirect("view_student")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def student(request,email):
    if request.user.is_accountant:
        if request.method=="POST":
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            Student.objects.filter(email=email).update(name=name, mobile_no=mobile, Gender=gender, Address=address, date_of_birth=dob)
            if request.FILES:
                profile = request.FILES['profile']
                faclty = Student.objects.get(email = email)
                os.remove(faclty.profile.path)
                faclty.profile = profile
                faclty.save()
            messages.success(request,"Update successfully!!!") 
            return redirect("view_student")
        studen = Student.objects.filter(email=email)
        print(studen)
        year = Year.objects.all()
        return render(request, "Accountant/view_studen_details.html",{"student":studen,"year":year})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def edit_accountant(request):
    if request.user.is_accountant:
        if request.method=="POST":
            user = Accountant.objects.get(id=request.user.id)
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            password = request.POST['password']
            l=user.set_password(password)
            user.save()
            username = request.user.email
            user=authenticate(email = username,password=password)
            if user:
                login(request, user)
            Accountant.objects.filter(email=request.user).update(name=name,Gender=gender,Address=address,mobile_no=mobile,date_of_birth=dob)
            messages.success(request,"Update successfully!!!") 
            return redirect("accountant_Dashboard")
        return render(request,"Accountant/edit_user.html")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")

@login_required(login_url='index')
def librarian_Dashboard(request):
    if request.user.is_library:
        notification = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False).count()
        assign_book = Assign_book.objects.filter(status="assign").count()
        book = Add_Book.objects.all().count()
        return render(request,"Librarian/librarian_Dashboard.html",{"notification":notification,"notification_count":notification_count,"assign_book":assign_book,"book":book})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def view_assig_Book(request):
    if request.user.is_library:
        notification = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False).count()
        view = Assign_book.objects.filter(status="assign")
        return render(request,"Librarian/View_assign_book.html",{"view":view,"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        else:
            return redirect("Student_Dashboard")


@login_required(login_url='index')
def Assign_Book(request):
    if request.user.is_library:
        notification = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False).count()
        if request.method=="POST":
            book = request.POST['Book']
            student = request.POST['name']
            assign_date = request.POST['assign_date']
            dua_date = request.POST['dua_date']
            b = Add_Book.objects.get(Book_name=book)
            b.quantity = int(b.quantity) -1
            b.save()
            name = Student.objects.get(name=student)
            Assign_book.objects.create(student=name,book=b,assign_date=assign_date,due_date=dua_date,status="assign")
            messages.success(request,"Book Assign")
            return redirect("view_assig_Book")
        Assign_student_name = Assign_book.objects.filter(status="assign")
        
        s = Student.objects.all()

        for student in Assign_student_name:
            s=s.exclude(id=student.student.id)
            
        a=date.today()
        
        book = Add_Book.objects.all()
        return render(request,"Librarian/Assign_book.html",{"student":s,"a":a,"Assign_student_name":Assign_student_name,"book":book,"notification":notification,"notification_count":notification_count})

    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def view_assign_book_details(request,id):
    if request.user.is_library:
        notification = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False).count()
        book = Assign_book.objects.filter(id=id)
        if request.method=='POST':
            statu = request.POST['status']
            Assign_book.objects.filter(id=id).update(status=statu)
            b= Assign_book.objects.get(id=id)
            b.book.quantity=int(b.book.quantity) +1
            b.book.save()
            return redirect("view_assig_Book")
        return render(request,"Librarian/view_assign_book_details.html",{"notification":notification,"notification_count":notification_count,"book":book[0]})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def Book(request):
    if request.user.is_library:
        notification = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False).count()
        book = Add_Book.objects.all()
        return render(request,"Librarian/View_Book.html",{"book":book,"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        else:
            return redirect("Student_Dashboard")

@login_required(login_url='index')
def add_book(request):
    notification = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False)
    notification_count = Notification.objects.filter(Q(whome="Librarian") | Q(whome="All")).filter(status=False).count()
    if request.user.is_library:
        if request.method=="POST":
            book = request.POST["Book"]
            publication = request.POST["publication"]
            quantity = request.POST["quantity"]
            Add_Book.objects.create(Book_name=book,publication=publication,quantity=quantity)
            messages.success(request,"Book Added Successfully")
            return redirect(Book)

        return render(request,"Librarian/Add_Book.html",{"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        else:
            return redirect("Student_Dashboard")



@login_required(login_url='index')
def edit_student(request):
    if request.user.is_student:
        if request.method=="POST":
            user = Student.objects.get(id=request.user.id)
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            password = request.POST['password']
            l=user.set_password(password)
            user.save()
            username = request.user.email
            user=authenticate(email = username,password=password)
            if user:
                login(request, user)
            Student.objects.filter(email=request.user).update(name=name,Gender=gender,Address=address,mobile_no=mobile,date_of_birth=dob)
            messages.success(request,"Update successfully!!!") 
            return redirect("accountant_Dashboard")
        return render(request,"Student/edit_user.html")
    else:
        if request.user.is_faculty:
            return redirect("Faculty_Dashboard")
        elif request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        else:
            return redirect("librarian_Dashboard")
@login_required(login_url='index')
def Faculty_Dashboard(request):
    if request.user.is_faculty:
        return render(request,"Faculty/faculty_dashboard.html")
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
        
@login_required(login_url='index')
def Add_marks(request):
    if request.user.is_faculty:
        notification = Notification.objects.filter(Q(whome="Faculty") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Faculty") | Q(whome="All")).filter(status=False).count()
        year = Year.objects.all()
        depart = Department.objects.get(faculty=request.user)
        
        if request.method=="POST":
            y = request.POST['a']
            year = Year.objects.filter(name=y)
            for i in year:
                student = Student.objects.filter(Q(year=i) & Q(department=depart)).values()
            st = list(student)
            return JsonResponse({'student':st})
        return render(request,"Faculty/Add_marks.html",{"year":year,"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def Save_marks(request):
    if request.user.is_faculty:
        if request.method=="POST":
            subject =  Subject.objects.filter(faculty=request.user)
            for i in subject:
                user = Faculty.objects.filter(subject=i)
            user=list(user)
            name=request.POST.getlist('name')
            marks=request.POST.getlist('marks')
            for i in range(len(name)):
                student = Student.objects.filter(id=name[i])
                Marks.objects.create(subject=subject[0],faculty=user[0],student=student[0],add_mark=marks[i])
            return redirect("Add_marks")
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def Add_attendance(request):
    if request.user.is_faculty:
        notification = Notification.objects.filter(Q(whome="Faculty") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Faculty") | Q(whome="All")).filter(status=False).count()
        year = Year.objects.all()
        depart = Department.objects.get(faculty=request.user)
        
        if request.method=="POST":
            y = request.POST['a']
            year = Year.objects.filter(name=y)
            for i in year:
                student = Student.objects.filter(Q(year=i) & Q(department=depart)).values()
            st = list(student)
            # st = list(student)
            return JsonResponse({'student':st})
        return render(request,"Faculty/Add_attendance.html",{"year":year,"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def edit_faculty(request):
    if request.user.is_faculty:
        if request.method=="POST":
            user = CustomeUser.objects.get(id=request.user.id)
            name = request.POST['Name']
            address = request.POST['address']
            gender = request.POST['gender']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            password = request.POST['password']
            l=user.set_password(password)
            user.save()
            username = request.user.email
            user=authenticate(email = username,password=password)
            if user:
                login(request, user)
            Faculty.objects.filter(email=request.user).update(name=name,Gender=gender,Address=address,mobile_no=mobile,date_of_birth=dob)
            messages.success(request,"Update successfully!!!") 
            return redirect("Faculty_Dashboard")
        notification = Notification.objects.filter(Q(whome="Faculty") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Faculty") | Q(whome="All")).filter(status=False).count()
        year = Year.objects.all()
        depart = Department.objects.get(faculty=request.user)
        
        
        return render(request,"Faculty/edit_user.html",{"year":year,"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")
@login_required(login_url='index')
def save_attendance(request):
    if request.user.is_faculty:
        if request.method=="POST":
            subject =  Subject.objects.get(faculty=request.user)
            # print(subject)
            name=request.POST.getlist('name')
            status=request.POST.getlist('status')
            for i in range(len(name)):
                student = Student.objects.get(id=name[i])
                Attendance.objects.create(subject=subject,student_id=student,status=status[i])
        return render(request,"Faculty/Add_attendance.html")
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Student_Dashboard")

@login_required(login_url='index')
def Student_Dashboard(request):
    
    if request.user.is_student:
        notification = Notification.objects.filter(Q(whome="Student") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Student") | Q(whome="All")).filter(status=False).count()
        return render(request,"Student/student_dashboard.html",{"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Faculty_Dashboard")

@login_required(login_url='index')
def attendance(request):
    
    if request.user.is_student:
        notification = Notification.objects.filter(Q(whome="Student") | Q(whome="All")).filter(status=False)
        notification_count = Notification.objects.filter(Q(whome="Student") | Q(whome="All")).filter(status=False).count()
        user = request.user.id
        
        attendance = Attendance.objects.filter(student_id=user)
        return render(request,"Student/view_attendance.html",{"attendance":attendance,"notification":notification,"notification_count":notification_count})
    else:
        if request.user.is_superuser:
            return redirect("Hod_dashboard")
        elif request.user.is_accountant:
            return redirect("accountant_Dashboard")
        elif request.user.is_library:
            return redirect("librarian_Dashboard")
        else:
            return redirect("Faculty_Dashboard")