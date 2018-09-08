from django.shortcuts import render, redirect
from .models import Schools, SchoolData
from .forms import SchoolDataForm,SchoolForm
# Create your views here.
def home(request):
    return render(request,'index.html')

def schooldata_list(request):
    schooldatas = SchoolData.objects.all()
    return render(request,'schooldata_list.html', {'schooldatas':schooldatas})

def schooldata_edit(request, id):
    print('ohhhh')
    schooldata=SchoolData.objects.get(id=id)
    return render(request,'schooldata_edit.html', {'schooldata':schooldata})
def test(request):
    return render(request, 'test.html')

def schooldata_delete(request, id):
    schooldata=SchoolData.objects.get(id=id)
    schooldata.delete()
    return redirect("/schooldata/show")
def add_show(request):
    return render(request, 'school_add.html')
def school_add(request):
    if request.method=="POST":
        form=SchoolForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/school/show')
            except:
                pass
        else:
            form=SchoolForm()
        return render(request,'school_add.html',{'form':form})


def schooldata_update(request, id):
    print('ohhhh')
    schooldata = SchoolData.objects.get(id=id)
    form = SchoolDataForm(request.POST, instance=schooldata)
    if form.is_valid():
        form.save()
        print('no_is_valid')
        return redirect("/schooldata/show")
    return render(request, 'schooldata_edit.html', {'schooldata': schooldata})