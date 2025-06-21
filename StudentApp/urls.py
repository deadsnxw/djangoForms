from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='StudentApp/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
]
