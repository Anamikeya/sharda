from django.shortcuts import render,redirect
from .models import files

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def uploadimage(request):
    print("done....")
    if request == 'POST':
        f = files()
        f.image = request.FILES['image']
        f.save()
        return render(request,'index.html')
    else:
        return render(request,'index.html')
    
    