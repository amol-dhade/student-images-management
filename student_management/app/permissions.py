from django.contrib.auth.decorators import user_passes_test

def teacher_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_role == 'Teacher',
        login_url='login'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def student_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_role == 'Student',
        login_url='login'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def admin_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_role == 'Admin',
        login_url='login'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator