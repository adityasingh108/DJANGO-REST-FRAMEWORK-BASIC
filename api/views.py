from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from . models import Student
from .serializers import Studentserializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
import io


# Create your views here.

def studentInfo_id(request ,id):
    # FOR MODEL OBJECT  use get and id and for for query set use many = True
    stu = Student.objects.get(id=id)
    serialzer  = Studentserializers(stu)
    # METHOD === 1
    
    # json_data = JSONRenderer().render(serialzer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    
    # METHOD == 2
    return JsonResponse(serialzer.data,safe=False)

def studentInfo(request):
    # FOR MODEL OBJECT  use get and id and for for query set use many = True
    stu = Student.objects.all()
    serialzer  = Studentserializers(stu ,many=True)
    # METHOD ++ 1
    
    # json_data = JSONRenderer().render(serialzer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    
    # METHOD ++ 2
    
    return JsonResponse(serialzer.data,safe=False)

@csrf_exempt
def CreateStudentInfo(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializers = Studentserializers(data = python_data)
        if serializers.is_valid():
            serializers.save()
            res = {'Message ':'Data has been created'}
            return JsonResponse(res)
        else:
            return JsonResponse(serializers.errors)
        
    
        