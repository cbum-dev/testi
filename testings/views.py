from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render(request,'index.html')

def boys1(request):
    context = {}
    labbi = Student.objects.all()
    context = {
        'boy': labbi,}
    return render(request, 'index.html', context)