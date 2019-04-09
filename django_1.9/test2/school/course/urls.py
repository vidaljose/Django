from django.conf.urls import url
from course.forms import StudentForm
from course import views

urlpatterns = [
    url(r'^list_student/',views.list_student , name = 'list_student'),
    url(r'^create_student/',views.StudentCreate.as_view() , name = 'create_student'),
    url(r'edit_student/(?P<pk>\d+)/$', views.StudentEdit.as_view(),name='edit_student')
]
