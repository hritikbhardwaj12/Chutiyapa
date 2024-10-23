from django.shortcuts import render
from datetime import datetime
from home.models import Sign_up as SignUpModel
# Create your views here.
	
def login(request):    
	return render(request,'login.html')
	
def forgot_password(request):
    return render(request,'forgot_password.html')
def sign_up(request):
    if request.method == "POST":
        College_Email = request.POST.get('College_Email')
        Gender=request.POST.get('Gender')
        Branch=request.POST.get('Branch')
        Year=request.POST.get('Year')
        
        sign_up_instance = SignUpModel(
            College_Email=College_Email,
            Gender=Gender,
            Branch=Branch,
            Year=Year,
            date=datetime.today()
            )
        sign_up_instance.save()
        return render(request,'Sign_up.html')
    return render(request, 'sign_up.html')

def Home(request):
    return render(request,'Home.html')
def logout(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
def setting(request):
    return render(request,'setting.html')
def login(request):    
	return render(request,'login.html')

