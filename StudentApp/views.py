from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Comment
from .forms import StudentForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

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

@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    template_name = 'StudentApp/student_detail.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.student = self.object
            comment.save()
            return redirect('student_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

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

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    comments = Comment.objects.filter(author=user).order_by('-created_at')
    return render(request, 'StudentApp/profile.html', {'profile_user': user, 'comments': comments})
