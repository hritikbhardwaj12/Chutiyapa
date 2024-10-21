from django.shortcuts import render
from datetime import datetime
from home.models import Sign_up
from django.contrib import messages
# Create your views here.
	
def login(request):    
	return render(request,'login.html')
	
def forgot_password(request):
    return render(request,'forgot_password.html')
def Sign_up(request):
    if request.method == "POST":
        College_Email = request.POST.get('College_Email')
        Gender=request.POST.get('Gender')
        Branch=request.POST.get('Branch')
        Year=request.POST.get('Year')
        Sign_up= Sign_up(College_Email=College_Email,Gender=Gender,Branch=Branch,Year=Year,date=datetime.today())
        Sign_up.save()
        return render(request,'Sign_up.html')
    def Home(request):
        return render(request,'Home.html')
    def logout(request):
        return render(request,'login.html')
    def profile(request):
        return render(request,'profile.html')
    def setting(request):
        return render(request,'setting.html')

