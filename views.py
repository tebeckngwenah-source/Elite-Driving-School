from django.shortcuts import render,redirect

def home_page(request):
    return render(request,'index.html')
def course_add(request):
    return render(request,'admin.html')
def users(request):
    return render(request,'User.html')