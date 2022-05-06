from django import forms

from . import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class EmpForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name = forms.CharField(min_length=5, label="name", error_messages={"required": "This field cannot be empty!",
                                                                    "min_length": "The user name is too short。"},validators=[alphanumeric])
    age = forms.IntegerField(label="age")
    r_salary = forms.DecimalField(max_digits=8,  label="Please enter your password again")
    email =forms.EmailField()
    number=forms.IntegerField(label="number")
    country=forms.CharField(max_length=20,label="country")


    def clean_name(self):
        val = self.cleaned_data.get("name")


        if val.isdigit():
            raise ValidationError("The user name cannot be a pure number")
        elif models.Emp.objects.filter(name=val):
            raise ValidationError("User name already exists!")
        else:
            return val

    def clean(self):
        val = self.cleaned_data.get("salary")
        r_val = self.cleaned_data.get("r_salary")


        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("Please confirm whether the wages are consistent.")