
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'department']

    

#     Explain
#     forms.Form - create a Django form
#     charfield - accept text
#     EmailField - validates email format
#     IntegerField - accepts integer values