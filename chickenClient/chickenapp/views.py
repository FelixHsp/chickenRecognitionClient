from django.shortcuts import render
from django.shortcuts import HttpResponse
from chickenClient import settings

def index(request):
    return render(request, 'index.html')

def info(request):
    if request.method == "POST":
        f1 = request.FILES['pic1']
        fname = '%s/pic/%s' % (settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
        return HttpResponse("ok")
    else:
        return HttpResponse("error")