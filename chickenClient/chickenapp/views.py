from django.shortcuts import render
from django.shortcuts import HttpResponse
from chickenClient import settings
from . import models
from . import prediction
def index(request):
    return render(request, 'index.html')

def info(request):
    if request.method == "POST":
        f1 = request.FILES['pic1']
        fname = '%s/pic/%s' % (settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)

        kind = prediction.testchicken(f1.name)
        chicken1 = models.chikenkind.objects.get(id=kind+1)
        return render(request, 'chickenkind.html', {'name': chicken1.name, 'feature': chicken1.feature,'img':f1.name,'show':chicken1.show,"text":chicken1.text})
    else:
        return HttpResponse("error")

def chickenkind(request):
    chicken1 = models.chikenkind.objects.get(id=1)
    return render(request,'chickenkind.html',{'name':chicken1.name,'feature':chicken1.feature,'img':'../pic/Screen Shot 2019-04-29 at 1.49.32 PM.jpg','show':chicken1.show,"text":chicken1.text})