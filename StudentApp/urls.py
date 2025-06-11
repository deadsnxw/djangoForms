from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]
