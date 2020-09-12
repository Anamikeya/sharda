from django.shortcuts import render,redirect
from django.contrib import messages
from .models import regitration

# Create your views here.
def register(request):
    if request.method == "POST":
        data = regitration()

        data.S_No = request.POST.get('S_No')
        data.Guide_Name = request.POST.get('Guide_Name')
        data.Project_Title = request.POST.get('Project_Title')
        data.Student_Name = request.POST.get('Student_Name')
        data.System_Id = request.POST.get('System_Id')
        data.Roll_No = request.POST.get('Roll_No')
        data.Team_size = request.POST.get('Team_Size')
        data.Project_Category = request.POST.get('Project_Category')
        data.Section = request.POST.get('Section')
        data.Project_Passcode = request.POST.get('Project_Passcode')
        data.Student_Email = request.POST.get('Student_Email')
        data.Phone_Number = request.POST.get('Phone_Number')
        data.Project_Form_Number = request.POST.get('Project_Form_Number')
        data.Pannel_Number = request.POST.get('Pannel_Number')
        data.Attendance_In_Eval_0 = request.POST.get('Attendance_In_Eval_0')
        data.Identification_of_problem_Domain = request.POST.get('Identification_Of_Problem_Domain')
        data.Knowledge_Of_Problem_Domain = request.POST.get('Knowledge_Of_Problem_Domain')
        data.Creativity_And_Originality_In_Problem = request.POST.get('Creativity_And_Originality_In_Problem')
        data.Knowledge_Purpose_And_Resource = request.POST.get('Knowledge_Purpose_And_Resource')
        data.Team_Size_As_Project_Size = request.POST.get('Team_Size_As_Project_Size')
        data.Project_Planning_And_Work_Distribution = request.POST.get('Project_Planning_And_Work_Distribution')
        data.Oral_Communication = request.POST.get('Oral_Communication')
        data.Quality_Of_Written_Proposal = request.POST.get('Quality_Of_Written_Proposal')
        data.Guide_Marks = request.POST.get('Guide_Marks')
        data.Quality_Of_Project_Title = request.POST.get('Quality_Of_Project_Title')
        data.Total = request.POST.get('Total')
        data.Remark= request.POST.get('Remark')
        
        messages.info(request,"Successfully Uploaded")

        data.save()
        return redirect('register')
    else:
        return render(request,'evaluation.html')