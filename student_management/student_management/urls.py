"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('teacher/', views.teacher_view, name='teacher'),
    path('student/', views.student_view, name='student'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard,name='student_dashboard'),
    path('admin/dashboard/', views.admin_dashboard,name='admin_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/image/', views.image_view, name='upload_images')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
