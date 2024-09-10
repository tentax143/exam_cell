from students.models import Student
from django.contrib.auth.forms import forms # type: ignore

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'rit']
