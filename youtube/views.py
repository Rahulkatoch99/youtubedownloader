from django.shortcuts import render
from django.contrib import messages
from pytube import *

# Create your views here.

def home(request):
    if request.method=='POST':
        url=request.POST['url']
        video= YouTube(url)
        stream=video.streams.get_highest_resolution()
        stream.download()
        messages.info(request,'Video Download.....')
        return render(request,'home.html')
    return render(request,'home.html')

