from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'surveyf/index.html')

def create(request, method=['POST']):
    request.session['name'] = request.POST['firstName']
    request.session['dojo'] = request.POST['dojolocation']
    request.session['language'] = request.POST['favlanguage']
    request.session['comment'] = request.POST['comment']
    return redirect('/submit')

def giveResults(request):
    return render(request, 'surveyf/results.html')
