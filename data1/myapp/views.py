from django.shortcuts import render
from myapp.models import myapp

# Create your views here.

def home(req):
   if req.method=='POST':
       name=req.POST['name']         
       email=req.POST['email']

       data1=myapp(name=name,email=email)
       data1.save()
       print('Data Saved...!')

   return render(req,'home.html')