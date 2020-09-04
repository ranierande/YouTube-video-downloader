from django.shortcuts import render, redirect
from pytube import YouTube
import os

url = ''

def ytb_down(request):
    return render(request, 'ytb_main.html')

def yt_download(request):
    global url
    url = request.GET.get('url')
    obj = YouTube(url)
    try:
       resolutions = []
       strm_all = obj.streams.filter(progressive=True, file_extension='mp4').all()
       for i in strm_all:
           resolutions.append(i.resolution)
           resolutions = list(dict.fromkeys(resolutions))
       embed_link = url.replace("watch?v=", "embed/")
       path = 'D:\\'
       print('resolutions :', resolutions)    
       return render(request, 'yt_download.html', {'rsl': resolutions, 'embd': embed_link, 'url': url})
    except:
           return render(request, 'sorry.html')   


def download_complete(request, res):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    print(f'DIRECT :', f'{dirs}/Downloads')
    if request.method == "POST":
       YouTube(url).streams.get_by_resolution(res).download(homedir + '/Downloads')
       return render(request, 'download_complete.html')
    else:
         return render(request, 'sorry.html')    
