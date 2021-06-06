from django.shortcuts import render, redirect
from .models import ConverterModel
from django.views.generic import View
from datetime import timezone
from .forms import ConverterForm, ReconvertForm
import time
from django.http import JsonResponse
import os, sys
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile 
import subprocess
# Create your views here.

def home(request):

    queued_files = ConverterModel.objects.filter(status='waiting').count() #or any kind of queryset
    failed_files = ConverterModel.objects.filter(status='error').count()
    converted_files = ConverterModel.objects.filter(status='done').count()
    processing = ConverterModel.objects.filter(status='processing').count()
    unavailable = ConverterModel.objects.filter(status='unavailable').count()
    all_files = ConverterModel.objects.all().count()
    context = {
        'tray':{ 'queued_files': queued_files, 
                  'failed_files' : failed_files, 
                   'converted_files' : converted_files, 
                    'processing': processing, 
                    'unavailable': unavailable, 
                    'all_files': all_files},
        'url': 'failed_doc',
        'tableID': '#dataTable',
    }
    print(context)
    return render(request, 'converter/home.html', context)

def file_count(request):

    queued_files = ConverterModel.objects.filter(status='waiting').count() #or any kind of queryset
    failed_files = ConverterModel.objects.filter(status='error').count()
    converted_files = ConverterModel.objects.filter(status='done').count()
    processing = ConverterModel.objects.filter(status='processing').count()
    unavailable = ConverterModel.objects.filter(status='unavailable').count()
    all_files = ConverterModel.objects.all().count()
    
    context = {
        'tray': [queued_files, failed_files, converted_files, processing, unavailable, all_files]
    }
    return render(request, 'partials/dashboard/_file_count.html', context)

def error_list(request):
    tray = query_helper.get_tray()
    error_ = tray.error

    list_ = {"data": [
        {
            "path": item,
            "full_path": os.path.join(tray.errored_files_destination, item)
        }
            
                 for item in error_
            ],
            'recordsTotal': len(error_),
            'recordsFiltered': len(error_), 
            "draw":1
            }
    return JsonResponse(list_, safe=False)

def status(request):
    # if request.is_ajax():
    queued_files = ConverterModel.objects.filter(status='waiting').count() #or any kind of queryset
    failed_files = ConverterModel.objects.filter(status='error').count()
    converted_files = ConverterModel.objects.filter(status='done').count()
    processing = ConverterModel.objects.filter(status='processing').count()
    unavailable = ConverterModel.objects.filter(status='unavailable').count()
    all_files = ConverterModel.objects.all().count()
    data = {
        'queued_files': queued_files, 
        'failed_files' : failed_files, 
        'done' : converted_files, 
        'processing': processing, 
        'unavailable': unavailable, 
        'all_files': all_files
    }
    return JsonResponse(data, safe=False)



def file_analysis(request):
    queued_files = ConverterModel.objects.filter(status='waiting').count() #or any kind of queryset
    failed_files = ConverterModel.objects.filter(status='error').count()
    converted_files = ConverterModel.objects.filter(status='done').count()
    processing = ConverterModel.objects.filter(status='processing').count()
    unavailable = ConverterModel.objects.filter(status='unavailable').count()
    all_files = ConverterModel.objects.all().count()
    data = {
        'queued_files': queued_files, 
        'failed_files' : failed_files, 
        'converted_files' : converted_files, 
        'processing': processing, 
        'unavailable': unavailable, 
        'all_files': all_files
    }
    return JsonResponse(data, safe=False)



class AllMediaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'url': 'all_doc',
            'type': 'All',
            'tableID': '#dataTable'
        }
        return render(request, 'converter/tablelist.html', context)

class ProcessedMediaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'url': 'done_doc',
            'type': 'Processed',
            'tableID': '#dataTable'            
        }
        return render(request, "converter/tablelist.html", context)

class QueuedMediaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'url': 'queued_doc',
            'type': 'Queued',
            'tableID': '#dataTable'
        }        
        return render(request, "converter/tablelist.html", context)

class FailedMediaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'url': 'failed_doc',
            'type': 'Failed',
            'tableID': '#dataTable',
        }        
        return render(request, "converter/tablelist.html", context)

class ProcessingMediaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'url': 'processing',
            'type': 'Processing',
            'tableID': '#dataTable',
        }        
        return render(request, "converter/tablelist.html", context)

class UnavailableMediaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'url': 'unavailable',
            'type': 'Unavailable',
            'tableID': '#dataTable',
        }        
        return render(request, "converter/tablelist.html", context)



class AddFileView(View):
    def get(self, request, *args, **kwargs):
        form = ConverterForm()
        context = {
            'form': form
        }        
        return render(request, "converter/new.html", context)
    def post(self, request, *args, **kwargs):
        form = ConverterForm(request.POST or None,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            media = data['media']
            name = media.name.split('.')
            input_ext = data['input_ext']
            output_ext = data['output_ext']
            print(name[0], name, output_ext)
            c = ConverterModel.objects.create(
                name=name[0],media=media,
                output_extension=output_ext,
                uploaded_extension=str('.' + name[-1])
            )
            return redirect('converter:file_detail',  pk=c.pk)
        else:
            print(form.errors)
            print('invalid')

class FileDetailView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        media = ConverterModel.objects.get(pk=pk)
        if media.output:
            output_url = media.output
            dirr = settings.BASE_DIR.replace('\\', '/') + "/btndom"
            print(dirr+output_url, "directory")
        form = ReconvertForm(initial={
            'output_ext': media.output_extension,
            'pk': pk
        })
        context = {
            'media': media,
            'form': form
        }
        return render(request, 'converter/detail.html', context)

def convert(request, pk):
    if request.is_ajax():
        pk = request.POST.get('pk')
        ext = request.POST.get('output_ext')
        obj = ConverterModel.objects.get(pk=int(pk))
        try:
            filePath = obj.media.path
        except:
            filePath = 'unavalile'
        mp4path = os.path.join(os.path.splitext(filePath)[0] + ext)

        if os.path.exists(os.path.join(os.path.splitext(filePath)[0] + obj.uploaded_extension)):
            if os.path.exists(mp4path):
                os.remove(mp4path)

            obj.status = 'processing'
            if ext in [".mp4", ".ts",".mkv" , ".flv"]:
                
                os.system("ffmpeg -y -i " + "\"" + filePath + "\""  + " \"" + mp4path + "\"")                
                # cmd = f"ffmpeg -y -i \"{filePath}\" \"{mp4path}\""
                # arch = os.system("ffmpeg -y -i " + "\"" + filePath + "\""  + " \"" + mp4path + "\"", shell=True)                
                # arch = subprocess.check_output(cmd, shell=True)                                
            elif ext in ['.mp3', '.m4a']:
                # cmd = f"ffmpeg -y -i \"{filePath}\" -vn -acodec copy \"{mp4path}\""
                cmd = f"ffmpeg -y -i \"{filePath}\" \"{mp4path}\""
                os.system(cmd)
                # os.system("ffmpeg -y -i " + "\"" + filePath + "\""  +" -vn -acodec copy " + " \"" + mp4path + "\"")
            final_path = mp4path.split("\\")[-3:]
            if os.path.exists(mp4path):
                print('done')
                string = "/"
                for f in final_path:
                    string += f +"/"
                obj.output = string.rstrip('/')
                obj.output_extension = ext
                obj.status = 'done'
                obj.save()
                data = {
                    'response': 'done',
                    'url': string.rstrip('/')
                }
                return JsonResponse(data)
            else:
                obj.status = 'error'
                obj.save()
                data = {
                    'response': 'error'
                }
                return JsonResponse(data)
        else:
            obj.status = 'unavailable'
            obj.save()
            data = {
                'response': 'unavailable',
                'alert': 'To be deleted soon'
            }
            return JsonResponse(data)
