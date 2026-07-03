from django import forms
from .models import Student,Course

class StudentForm(forms.ModelForm):
    courses=forms.ModelMultipleChoiceField(queryset=Course.objects.all(),widget=forms.SelectMultiple)
    class Meta:
        model = Student
        fields = ['name','email','enrollment','contact','courses']



        

