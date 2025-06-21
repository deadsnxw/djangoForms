from django import forms
from .models import Student, Comment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']