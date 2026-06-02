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
    data={
        'cfees':[5000,7000,3000,4000,2000],
        'cname':['python','java','php','html','css']
    }
    d='75 days'
    id=3
    fees=45000
    result=45
    return render(request,'course.html',{'id':id,'d':d,'fees':fees,'result':result,'data':data})


