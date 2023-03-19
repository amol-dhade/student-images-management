from django.shortcuts import render, redirect
from .models import Student, Teacher, Images, CustomUser
from .permissions import teacher_required, student_required, admin_required
from .forms import UserRegistrationForm, StudentForm, TeacherForm, ImageForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages


def signup_view(request):
    form = UserRegistrationForm
    template_name = 'app/signup.html'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login')
    
    
@teacher_required
def teacher_view(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)
            user = request.user
            teacher.user = user
            teacher.save()
    else:
        form = TeacherForm()
    return render(request, 'app/teacher_form.html', {'form':form})


@student_required
def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
    else:
        form = StudentForm()
    return render(request, 'app/student_form.html', {'form':form})


@student_required
def student_dashboard(request):
    user = request.user 
    student = Student.objects.filter(user=user)
    image = Images.objects.filter(user=user)
    context = {'student':student, 'image':image}
    return render(request, 'app/student_dashboard.html', context)
            
            
@teacher_required
def teacher_dashboard(request):
    user = request.user
    print(user)
    teacher = Teacher.objects.get(user=user)
    student = Student.objects.filter(teacher=teacher)
    image = Images.objects.filter(user=user)
    context = {'student':student, 'teacher':teacher, 'image':image}
    return render(request, 'app/teacher_dashboard.html', context)


@admin_required
def admin_dashboard(request):
    teacher = Teacher.objects.all()
    student = Student.objects.all()
    image = Images.objects.all()
    context = {'teacher':teacher, 'student':student, 'image':image}
    return render(request, 'app/admin_dashboard.html', context)


@login_required
def dashboard(request):
    if request.user.user_role == 'Admin':
        return admin_dashboard(request)
    elif request.user.user_role == 'Teacher':
        return teacher_dashboard(request)
    elif request.user.user_role == 'Student':
        return student_dashboard(request)
 
    
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'app/login.html')


@login_required
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = form.save(commit=False)
            images.user = request.user
            images.save()
    else:
        form = ImageForm()
    return render(request, 'app/upload_image.html', {'form':form})


def welcome_view(request):
    user = CustomUser.objects.filter(email=request.user)
    return render(request, 'app/welcome_page.html')
    
    

    
