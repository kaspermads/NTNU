from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData
from .models import Pasient
from django.template import loader


# Create your views here.

def test1(request):
    template = loader.get_template('test1.html')
    return HttpResponse(template.render())


def test2(request):
    mypasienter = Pasient.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        "mypasienter": mypasienter
    }
    return HttpResponse(template.render(context, request))

def pasient_data(request, id):
    mypasienter = Pasient.objects.get(id=id)
    
"""
@csrf_exempt
def receieve_data(request):s
    if request.method == "POST":
        data = request.POST
        sensor_data = SensorData()
        sensor_data.temperate = data["temperate"]
        sensor_data.pulse = data["pulse"]
        sensor_data.save()

        return JsonResponse({"success": True}, status=201)
    else:
        return JsonResponse({"error": "only POST method allowed"}, status=400)


def show_data(request):
    data = SensorData.objects.all()
    return render(request, 'show_data.html', {'data': data})"""
