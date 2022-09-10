from django.db.models.query import QuerySet
from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
from .models import *
def home(request):  
   template = loader.get_template('home.html') # getting our template  
   return HttpResponse(template.render())
   
def whoweare(request):  
   template = loader.get_template('whoweare.html') # getting our template  
   return HttpResponse(template.render())       
def contact(request):  
   if request.method=="POST":
       name=request.POST['name']
       email=request.POST['email']
       message=request.POST['message']
       ins=Contact(name=name,email=email,message=message)
       ins.save()
       
       
   return render(request,'../templates/contact.html')       
def recherche(request):
   country= Country.objects.all()
   speciality= Speciality.objects.all()
   
  
   if request.method=="POST":
      countri=request.POST.get('country')
      spec=request.POST.get('speciality')
      worker=Worker.objects.raw('select * from worker where country="'+countri+'" and speciality="'+spec+'"')

      ctx={'country':country,'speciality':speciality,'worker':worker}
      return render(request,'../templates/recherche.html',ctx)
   else:
       worker=Worker.objects.raw("select * from worker")
       ctx={'country':country,'speciality':speciality,'worker':worker}
       return render(request,'../templates/recherche.html',ctx)

def compte(request): 
   if request.method=="POST":
      
      cin=request.POST['cin']
      name=request.POST['name']
      lastname=request.POST['lastname']
      countryy=request.POST['country']
      phone=request.POST['phone']
      mail=request.POST['mail']
      specialityy=request.POST['speciality']
      ins=Worker(cin=cin,name=name,lastname=lastname,country=countryy,phone=phone,mail=mail,speciality=specialityy)
      ins.save()
      print("You are registered successfully!!")

   country= Country.objects.all()
   speciality= Speciality.objects.all()
   ctx={'country':country,'speciality':speciality}
   return render(request,'../templates/compte.html',ctx)   