from django.contrib import admin
from .models import AreaOfStudy, Pathway, Degree, Class, Student

# Register your models here.
admin.site.register(AreaOfStudy)
admin.site.register(Pathway)
admin.site.register(Degree)
admin.site.register(Class)
admin.site.register(Student)
