from django.contrib import messages
from django.shortcuts import redirect, render
from .fakers import *
from django.core.paginator import Paginator

def Populate(request):
    if request.method == 'POST':
        n=request.POST.get('data')
        np=int(n)
        for i in range(np):
            frollno=randint(1,500)
            fname=faker.name()
            faddress=faker.city()
            fmarks=randint(1,100)
            stu_record=Student.objects.get_or_create(rollno=frollno,name=fname,address=faddress,marks=fmarks)
        messages.success(request,'Data Created Successfullyy...!!!!')
        return redirect('populate')
    template_name='fakedata.html'
    return render(request,template_name)

def Paginationshowview(request):
    stu=Student.objects.all()
    paginator=Paginator(stu,10)
    page_no=request.GET.get('page',1)
    obj=paginator.get_page(page_no)
    template_name='pagination.html'
    context={'obj':obj}
    return render(request,template_name,context)

