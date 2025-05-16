from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    StudentApp = Student.objects.all()
    return render(request, 'StudentApp/student_list.html', {'students': StudentApp})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'StudentApp/student_add.html', {'form': form})