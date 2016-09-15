from django.shortcuts import render, redirect
import random, string

# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] = 1

    request.session['randWord'] = ''
    request.session['randWord'] = '-'.join(random.choice(string.uppercase) for i in xrange(14))

    return render(request, 'rand_word/index.html')
