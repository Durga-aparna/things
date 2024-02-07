import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from buses.models import bus
from api.v1.serializers import carSerializer
@csrf_exempt
def bus_details(request):
    if request.method=='GET':
        result=bus.objects.all()
        serializer=carSerializer(result,many=True)
        if serializer.is_valid:
            return JsonResponse(serializer.data,safe=False)
        else:
            return  HttpResponse("error occured")
    return HttpResponse("invalid details") 

    elif request.method=="POST":
        data=JSONParser().parse(request)
        serializer=carSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    return HttpResponse("Invalid Request method")  
@csrf_exempt
def  Bus_details(request):
    if request.method=="PATCH":
        data=JSONParser().parse(request)
        pk=data.get("id")
        obj=bus.objects.get(id=pk)
        serializer=carSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    return HttpResponse("Invalid Request method") 
@csrf_exempt
def  vehicle_details(request):
    if request.method=="PUT":
        data=JSONParser().parse(request)
        pk=data.get("id")
        obj=bus.objects.get(id=pk)
        serializer=carSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    return HttpResponse("Invalid Request method")  
@csrf_exempt
def edit_details(request):
    if request.method=="DELETE":
        data=JSONParser().parse(request)
        pk=data.get("id")
        obj=bus.objects.get(id=pk)
        obj.delete()
    return HttpResponse("deleted successfully") 
@csrf_exempt
def dynamic(request,V_NUM):
    if request.method=="GET":
        obj=bus.objects.get(number=V_NUM)
        data= carSerializer(obj)
        if data.is_valid:
            return JsonResponse(data.data,status=201)
        return JsonResponse(data.errors,status=400)
    return HttpResponse("Invalid data....")        








    
