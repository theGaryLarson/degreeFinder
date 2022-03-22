from django import forms
from .models import AreaOfStudy, Pathway, Degree, Class, Student


class AreaOfStudyForm(forms.ModelForm):
    class Meta:
        model = AreaOfStudy
        fields = '__all__'


class PathwayForm(forms.ModelForm):
    class Meta:
        model = Pathway
        fields = '__all__'


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = '__all__'


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
