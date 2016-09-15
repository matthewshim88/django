from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.

current_date = datetime.datetime.now()

def index(request):
    print current_date
    context={
        "time":current_date
    }
    return render(request, 'timedisplay/index.html', context)
