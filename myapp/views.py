from django.shortcuts import render, redirect
from .forms import EmpForm
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .import models

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "polls/from.html", {"form":form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect('/admin')
        else:
            clear_errors = form.errors.get("all")
            return render(request, "polls/from.html", {"form": form, "clear_errors": clear_errors})


def send_message(request):
    email=EmailMessage(
              "Web programming:back end",
              "My content",
              "26072019oppo@gmail.com",
              ['26072019oppo@gmail.com','200103520@stu.sdu.edu.kz'],
              headers={'Message-ID':'foo'},
        )

    email.send(fail_silently=False)
    return render(request,'polls//success.html')
