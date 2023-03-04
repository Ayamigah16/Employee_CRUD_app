from django import forms        # importing forms class
from employee.models import Employee        # importing Employee table from models.py in employee app

# creating the modelform
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee        # referencing Employee table
        fields = "__all__"      # applying all columns
        