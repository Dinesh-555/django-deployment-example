from django.shortcuts import render
#from apptwo.models import Users
from apptwo.forms import New_userForm
def index(request):
    return render(request,'index.html')
def users(request):
    form=New_userForm()
    if request.method=="POST":
        form=New_userForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error:Form Invalid")
    return render(request,'users.html',{'form':form})
# Create your views here.
