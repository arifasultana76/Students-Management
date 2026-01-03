from django.shortcuts import render , redirect
from myapp.models import *

def studentlist(request):
    student_data=StudentModel.objects.all()
    context={
        'student':student_data
    }
    return render(request,'studentlist.html',context)

def students(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Roll=request.POST.get('roll')
        Department=request.POST.get('department')
        Email=request.POST.get('email')
        Dob=request.POST.get('dob')
        
        StudentModel.objects.create(
            name = Name,
            roll = Roll,
            department = Department,
            email = Email,
            dob = Dob
            
        ).save()
        return redirect('studentlist')
    return render(request,'students.html')

def home(request):
    return render(request,'base.html')


        
    
    
