from django.contrib import admin
from .models import Student, Teacher, Images, CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'name','mobile', 'user_role' ]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'user']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'teacher']
    
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id','user','image']
    

