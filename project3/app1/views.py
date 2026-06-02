from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    id=[1,2,3,4]
    name=['A','B','C','D']
    data={
        'id':id,
        'name':name
    }
    return render(request,'about.html',{'data':data})

def course(request):
    coursename='python'
    d='75 days'
    id=3
    fees=45000
    result=85
    return render(request,'course.html',{'coursename':coursename,'id':id,'d':d,'fees':fees,'result':result})
