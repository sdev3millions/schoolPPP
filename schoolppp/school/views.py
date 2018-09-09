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
def schooldata_update(request, id):
    print('ohhhh')
    schooldata=SchoolData.objects.get(id=id)
    form = SchoolDataForm(request.POST, instance=schooldata)
    if form.is_valid():
        form.save()
        print('no_is_valid')
        return redirect("/")
    return render(request, 'schooldata_edit.html', {'schooldata': schooldata})
# def schooldata_show(request):
#     schools=Schools.objects.all()
#     return render(request,'schooldata_creat.html',{'schools':schools})
# def school_list(request):
#     schools=Schools.objects.all()
#     return render(request, 'school_list.html',{'schools':schools})
# def add_show(request):
#     return render(request, 'school_add.html')
def school_show(request):
    schools=Schools.objects.all()
    return render(request,'school_list.html',{'schools':schools})
def add_view(request):
    return render(request,'school_create.html')
def school_create(request):
    if request.method=="POST":
        form=SchoolForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print('add school')
                return redirect("/school/list")
            except:
                pass
        else:
            form=SchoolForm()
    return render(request,'school_add.html',{'form':form})
def school_delete(request,id):
    school=Schools.objects.get(id=id)
    school.delete()
    return redirect("/school/list")
def school_edit(request, id):
    print('ohhhh')
    school=Schools.objects.get(id=id)
    return render(request,'school_edit.html', {'school':school})
def school_update(request, id):
    print('ohhhh')
    school=Schools.objects.get(id=id)
    form = SchoolDataForm(request.POST)
    if form.is_valid():
        form.save()
        print('no_is_valid')
        return redirect("/school/list")
    return render(request, 'school_edit.html', {'school': school})