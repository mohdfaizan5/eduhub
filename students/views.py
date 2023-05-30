# This views.py is for request and response handling

from django.shortcuts import render
from .models import Student, Notes
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddForm



# Create your views here.
def index(request):
    return render(request, "students/crm.html", {
        "students": Student.objects.all()
    })

def student(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, "students/student.html", {
        "student": student
    })

def add(request):
    
    if request.method == "POST":
        form = AddForm(request.POST)
        print("got data from post")
        if form.is_valid():
            usn_number = form.cleaned_data["usn_number"]
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            gpa = form.cleaned_data["gpa"]
            new_student = Student(usn_number=usn_number, name=name, subject=subject, email=email, gpa=gpa)
            new_student.save()
            return HttpResponseRedirect(reverse("add"), {
                "success": False,
                "form": form
            })
        else:
            return render(request, "students/add.html", {"form": AddForm()})

    return render(request, "students/add.html", {"form": AddForm()})

def home(request):
    return render(request, "students/home.html")

def delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return HttpResponseRedirect(reverse("index"))

def contact(request):
    return render(request, "students/contact.html")
# def edit(request, student_id):
#     if request.method == "POST":
#         student = Student.objects.get(id=student_id)
#         form = AddForm(request.POST, instance=student)

#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect(reverse("edit"))
#             return render(request, "students/edit.html", {
#                 "success": True,
#                 "form": form
                    
#                 })
#     else:
#         student = Student.objects.get(id=student_id)
#         form = AddForm(request.GET,  instance=student)
#         return render(request, "students/edit.html", {"form": form})

def edit(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(pk=student_id)
        form = AddForm(request.POST)
        if form.is_valid():
            # form.save()
            return render(request, "students/edit.html", {
                "form": form,
                "success": True,
                "student": student
            })

    else:
        student = Student.objects.get(pk=student_id)
        # form = AddForm(instance= student)

    # return HttpResponseRedirect(reverse("edit"), {
    #     "form": form
    # })

    # else
    
    return render(request, "students/edit.html", {"form": AddForm()})



def notes(request):
    return render(request, "students/notes.html", {
        "notes": Notes.objects.all()
    })