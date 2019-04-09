from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView , UpdateView
from course.forms import StudentForm
from django.shortcuts import render
from course.models import Student

def list_student(request):
    student = Student.objects.all()
    return render(request, template_name='list_student.html', context={'student':student})

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    
    def get_success_url(self):
        return reverse('course:list_student')

class StudentEdit(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'

    def get_success_url(self):
        return reverse('course:list_student')

