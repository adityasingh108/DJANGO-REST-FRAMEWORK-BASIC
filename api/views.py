from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from . models import Student
from .serializers import Studentserializers
from rest_framework.renderers import JSONRenderer

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