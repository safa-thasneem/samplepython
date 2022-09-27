from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.
def demo(request):
   obj=place.objects.all()
   obj1=team.objects.all()
   return render(request,"index.html",{'result':obj,'result1':obj1})
# def registration(request):
#    if request.method=="POST" :
#       username=request.POST['UserName']
#       firstname = request.POST['FirstName']
#       lastname = request.POST['LastName']
#       email = request.POST['Email']
#       password = request.POST['Password1']
#       password = request.POST['Password2']
#       user=User.objects.create_user(username=UserName,password=Password,firstname=FirstName,lastname=LastName,email=Email)
#
#       user.save();
#       print("user created")
#
#    return render(request,"registration.html")
# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res1=x+y
#    res2=x-y
#    res3=x*y
#    res4=x/y
#    return render(request,"index.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

# def about(request):
#     return render(request,"index.html")
# def contact(request):
#     return HttpResponse("my contact")
# def details(request):
#     return render(request,"index.html")
# def thank(request):
#     return HttpResponse("thankyou")
