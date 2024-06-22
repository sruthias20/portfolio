from django.shortcuts import render
from Base import models
from Base.models import Contact 
from django.contrib import messages

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

       if len(name)>1 and len(name)<30:
           pass
       else:
           messages.error(request,'Lenght of name should be greater than 2 and less than 30 words ')
           return render(request,'home.html')
       
       if len (email)>1 and len(email)<30:
           pass
       else:
           messages.error(request,'Invaild email try again ')
           return render(request,'home.html')
       print(len(number))
       if  len(number)>9 and len(number)<13:
           pass
       else:
           messages.error(request,'Invaild number please try again ')
           return render(request,'home.html')
       babu = models.Contact(name=name,email=email,content=content,number=number)
       babu.save()
       messages.success(request,'Thank You for contacting me!! Your message has been saved ')
       print('Data has been saved to database')
 
       print('No pass ')
   return render(request,'home.html') 


