from django.shortcuts import render
from .models import Schools,SchoolData
from .forms import SchoolForm
# Create your views here.

def home(request):
    return render(request,'index.html')
def school_list(request):
    schooldatas = SchoolData.objects.all() 
    return render(request,'school/schooldata_list.html', {'schooldatas':schooldatas})
def school_edit(request, id):
    schooldata=SchoolData.objects.get(id=id) 
    return render(request,'school/schooldata_edit.html', {'schooldata':schooldata}) 
