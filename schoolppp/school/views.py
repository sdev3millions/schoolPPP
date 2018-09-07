from django.shortcuts import render
# Create your views here.
from .models import SchoolData, School
def home(request):
    return render(request,'index.html')
def school_list(request):
    schools=School.objects.all()
    return render(request,'schooldata_list.html', {'school':})