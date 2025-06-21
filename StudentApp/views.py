from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class StudentDetailView(DetailView):
    model = Student
    template_name = 'StudentApp/student_detail.html'
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'StudentApp/student_update.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'StudentApp/student_delete.html'
    success_url = reverse_lazy('student_list')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form = UserCreationForm()
    return render(request, 'StudentApp/register.html', {'form': form})
