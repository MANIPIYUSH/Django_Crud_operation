from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp


def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        emp_id=request.POST.get("emp_id")
        emp_name=request.POST.get("emp_name")
        emp_dob=request.POST.get("emp_dob")
        emp_doj=request.POST.get("emp_doj")
        emp_department=request.POST.get("emp_department")
        emp_post=request.POST.get("emp_post")
        emp_address=request.POST.get("emp_address")
        emp_city=request.POST.get("emp_city")
        emp_zipcode=request.POST.get("emp_zipcode")
        emp_state=request.POST.get("state")
        emp_onleave=request.POST.get("on_leave")
       
        e=Emp()
        e.emp_id=emp_id
        e.name=emp_name
        e.dob=emp_dob
        e.doj=emp_doj
        e.department=emp_department
        e.post=emp_post
        e.address=emp_address
        e.city=emp_city
        e.zip=emp_zipcode
        e.state=emp_state
       
        if emp_onleave is None:
            e.onleave=False
        else:
            e.onleave=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    print("Ok!")
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_id_temp=request.POST.get("emp_id")
        emp_name=request.POST.get("emp_name")
        emp_dob=request.POST.get("emp_dob")
        emp_doj=request.POST.get("emp_doj")
        emp_department=request.POST.get("emp_department")
        emp_post=request.POST.get("emp_post")
        emp_address=request.POST.get("emp_address")
        emp_city=request.POST.get("emp_city")
        emp_zipcode=request.POST.get("emp_zipcode")
        emp_state=request.POST.get("state")
        emp_onleave=request.POST.get("on_leave")
       

        e=Emp.objects.get(pk=emp_id)
        
        e.emp_id=emp_id_temp
        e.name=emp_name
        e.dob=emp_dob
        e.doj=emp_doj
        e.department=emp_department
        e.post=emp_post
        e.address=emp_address
        e.city=emp_city
        e.zip=emp_zipcode
        e.state=emp_state
        
        if emp_onleave is None:
            e.onleave=False
        else:
            e.onleave=True
        e.save()
    return redirect("/emp/home/")
