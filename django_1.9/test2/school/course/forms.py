from django import forms
from course.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'subject_student': forms.SelectMultiple(attrs={'class':'form-control'})
        }
