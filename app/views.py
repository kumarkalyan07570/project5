from django.shortcuts import render
date='this data is a assumption'
name='kalyan'
age=20
gmail='kalyan com'
d={'assumption':date,'username':name, 'age':20,'gmail':gmail}

# Create your views here.
def data(request):
    return render(request,'data.html',context=d)

def login(request):
    return render(request,'data.html',context=d)

def webpages(request):
    return render(request,'data.html',context=d)




    
