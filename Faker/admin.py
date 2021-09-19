from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display=['id','rollno','name','address','marks']
admin.site.register(Student,StudentAdmin)
