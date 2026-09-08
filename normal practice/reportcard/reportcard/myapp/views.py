from django.shortcuts import render
from myapp.models import *
from django.core.paginator import Paginator
from django.db.models import Sum,Count,Q
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings 
# Create your views here.
def index(request):
    students = Student.objects.all()
    paginator =Paginator(students, 5)

    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    return render(request,"index.html",{"students":page_object})

def report(request):
    id = request.GET['id']
    action = request.GET['action']
    data = Marks.objects.filter(student_id=id)

    all = Student.objects.annotate(
        total_marks=Sum('marks_marks'),

        

        )
    )