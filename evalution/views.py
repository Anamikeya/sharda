from django.shortcuts import render,redirect
from .models import data
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        #if request.POST.get('Full_Name') and request.POST.get('System_id') and request.POST.get('Roll_No') and request.POST.get('Email') and request.POST.get('Project_Title') and request.POST.get('Guide_Name') and request.POST.get('Team_Size') and request.POST.get('Project_Category') and request.POST.get('Section') and request.POST.get('Project_Passcode') and request.POST.get('Phone_Number') and request.POST.get('Submitted_Sypnosis') and request.POST.get('Screenshot_Of_Approval'):
            datas = data()

            datas.Full_Name = request.POST.get('Full_Name')
        
            datas.System_id = request.POST.get('System_id')
            datas.Roll_No =request.POST.get('Roll_No')
            datas.Email = request.POST.get('Email')
            datas.Project_Title = request.POST.get('Project_Title')
            datas.Guide_Name = request.POST.get('Guide_Name')
            datas.Team_Size = request.POST.get('Team_Size')
            datas.Project_Category =request.POST.get('Project_Category')
            datas.Section = request.POST.get('Section')
            datas.Project_Passcode = request.POST.get('Project_Passcode')
            datas.Phone_Number = request.POST.get('Phone_Number')
            datas.Submitted_Sypnosis = request.POST.get('Submitted_Sypnosis')
            
            
            datas.save()
            messages.info(request,"successfully uploaded")
            # deepcode ignore PythonDeadCode: <please specify a reason of ignoring this>
            return redirect('/')
            
            
    else:    
            return render(request,"final.html")
    
  
    