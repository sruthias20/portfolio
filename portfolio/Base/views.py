from django.shortcuts import render
from Base import models
from Base.models import Contact 

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
   if request.method=="POST":
       print('post')
       name=request.POST.get('name')
       email=request.POST.get('email')
       number=request.POST.get('number')
       content=request.POST.get('content')
       print(name,email,number,content )
