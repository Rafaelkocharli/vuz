from django.shortcuts import render, HttpResponse
from .models import University, Faculty
import math

subjects = [
    'mathematics',
    'chemistry',
    'social',
    'history',
    'foreignlanguage',
    'biology',
    'geography',
    'physics',
    'informatics',
    'literature'
]

def index(request):
    if request.method == 'POST':
        f, s = int(request.POST.get('first')), int(request.POST.get('second'))
        page = int(request.POST.get('page'))
        split = int(request.POST.get('split'))
        if s-1 == -1:
            first = subjects[f-1]
            olddata = list(University.objects.filter(first=first, second='').values())
            data = olddata[(page-1)*split:split*page]
            maxpage = math.ceil(len(olddata)/split)
        return render(request, 'data.html', context={
            'data':data,
            'page':page,
            'split':split,
            'f':f,
            's':s,
            'maxpage':maxpage
                                                     })
    return render(request, 'main.html')