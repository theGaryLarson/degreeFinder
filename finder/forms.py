from django import forms
from .models import AreaOfStudy, Pathway, Degree, Class, Student


class AreaOfStudyForm(forms.ModelForm):
    class Meta:
        model = AreaOfStudy
        fields = '__all__'  # ['area_of_study', 'description']


class PathwayForm(forms.ModelForm):
    class Meta:
        model = Pathway
        fields = '__all__'   # ['area', 'subject', 'description', 'revised_date']


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ['pathway', 'title', 'description', 'contact', 'guide', 'grants']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
