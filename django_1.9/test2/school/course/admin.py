from django.contrib import admin

from course.models import Subject,Student

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','number_credits')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','lastname')

admin.site.register(Student,StudentAdmin)
admin.site.register(Subject,SubjectAdmin)
