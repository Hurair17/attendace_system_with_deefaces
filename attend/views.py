from django.shortcuts import render,redirect
# Create your views here.
import pandas as pd
from .function.takepicfun import takepicture
from .function.call_real_data_deepface import stream
from .models import NameDate,SaveImage
from django.core.files.base import ContentFile

#for creating file from image to copy
# def creatinFileObject(file,name):
#     content_file = ContentFile(file,name=name)
#     return content_file


def home(request):
    return render(request,'home.html')

def takepic_screen(request):
    return render(request,'takepic.html')

def cameraopen(request):
    name = request.POST.get('name')
    department = request.POST.get('department')
    email = request.POST.get('email')
    
    list_of_path,img_name = takepicture(name)
    for i in range(len(list_of_path)):
        # image = list_of_path[i].split('/')
        # image = image[:3]
        # file = creatinFileObject(list_of_path[i],image)
        model = SaveImage.objects.create(name = img_name,department=department,email=email, image = list_of_path[i])
        model.save()
    return redirect('/')

def attendance(request):
    name_and_date = stream()
    ename = name_and_date[0]
    date = name_and_date[1]
    # given_name = name
    departmnet_name = ''
    # employee = SaveImage.objects.filter(name = ename)
    # for i in employee:
    #     departmnet_name = i.department
    # print(departmnet_name)
    for i in range(len(ename)):
        model = NameDate(name = ename[i],date=date[i],department = departmnet_name)
        model.save()
    return redirect('/')

def attendDataHtml(request):
    # path = 'D:/JMM/00 EXCEL/attend.csv'
    # df = pd.read_csv(path)
    employee = NameDate.objects.all
    return render(request,'total_data.html',{'employee':employee})
    # return render(request,'total_data.html',{'df':df})
