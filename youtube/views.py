from django.shortcuts import render
from django.contrib import messages
from pytube import *
from pytube.cli import on_progress

# Create your views here.

def home(request):
    if request.method=='POST':
        url=request.POST['url']
        video= YouTube(url,on_progress_callback=on_progress)
        stream=video.streams.get_highest_resolution()
        stream.download("/storage/emulated/0/Download")
        messages.info(request,'Video Download.....')
        return render(request,'home.html')
    return render(request,'home.html')

