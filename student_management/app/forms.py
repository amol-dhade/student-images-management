from django import forms 
from .models import Student, CustomUser, Teacher, Images
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password1', 'password2', 'mobile', 'user_role')
        
        labels = {
            'name':'Name',
            'password1':'Password',
            'password2':'Confirm Password',
            'mobile':'Mobile',
            'user_role':'User Role'
        }
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'user_role':forms.Select(attrs={'class':'form-control'
                                            })
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']
    
        
class TeacherForm(forms.ModelForm):  
    class Meta:
        model = Teacher 
        fields = ['name','subject']
        
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'image_title']
        
        
        

        
        