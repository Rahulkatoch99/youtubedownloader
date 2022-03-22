from django.shortcuts import render
from django.contrib import messages
from pytube import YouTube
from pytube.cli import on_progress
import sys,os


# Create your views here.

# # Create your views here.
# def createDirectory(name):
#     path=sys.path[0]
#     if not(os.path.isdir(f'{path}/{name}')):
#         path =os.path.join(sys.path[0],name)
#         os.mkdir(path)
# directoyName='video'
# createDirectory(directoyName)
# path=sys.path[0]
def home(request):
    if request.method=='POST':
        url=request.POST['url']
        video= YouTube(url,on_progress_callback=on_progress)
        stream=video.streams.get_highest_resolution()

        # vid=list(enumerate(stream))
        # for i in vid:
        #     print()
        # save_path='/downloads/'
        # ch=int(input())
        stream.download("C:/Users/Rahul/Downloads")
        # stream.download("/Downloads")
        messages.info(request,'Video Download.....')
        return render(request,'home.html')
    return render(request,'home.html')

