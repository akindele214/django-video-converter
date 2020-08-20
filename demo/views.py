from django.shortcuts import render
from django.http import JsonResponse
import time
from .models import DemoTS
from django.http import HttpResponse
from django.core import serializers
import os
import sys

# Create your views here.

def test(request):
    if request.is_ajax():
        pk = request.GET.get('id')
        obj = DemoTS.objects.get(pk=pk)
        filePath = obj.media.path
        mp4path = os.path.join(os.path.splitext(filePath)[0] + ".mp4")
        obj.is_processing = True
        obj.save()
        sql = """
                INSERT INTO public.records_location_small
                (id, "date", "hour", channel, pc_name, ip, filename, alive)
                
            """

        if os.path.isfile(mp4path):
            print(mp4path)
        os.system("ffmpeg -y -i " + "\"" + filePath + "\""  + " \"" + mp4path + "\"")
        final_path = mp4path.split("\\")[-3:]
        string = "/"
        for f in final_path:
            string += f +"/"

        obj.download_url = string
        obj.is_ready = True
        obj.is_processing = False
        obj.save()
        sql += "("+ str([obj.pk, '2020-08-19', 19, 93, 'tv', '192.168.1.11', string, 1]) + ")"
        context = {
            "url": string,
            "sql": sql
        }
        data = string
    return JsonResponse(context, safe=False)

def processing(request):
    if request.is_ajax():
        pk = request.GET.get('id')
        obj = DemoTS.objects.get(pk=pk)
        is_ready = False
        if obj.is_ready:
            is_ready = True
            url = obj.download_url
        else:
            url = ""
        context = {
            'url': url,
            'is_ready': is_ready
        }
    return JsonResponse(context, safe=False)



def myModel_asJson(request):
    object_list = DemoTS.objects.all() #or any kind of queryset
    json = serializers.serialize('json', object_list)
    print(json)
    return HttpResponse(json, content_type='application/json')