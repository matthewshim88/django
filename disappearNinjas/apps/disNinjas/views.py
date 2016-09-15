from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'disNinjas/index.html')

def allNinjas(request):
    imagelist = ['purple.jpg', 'blue.jpg', 'orange.jpg', 'red.jpg']
    context = {
        'images': imagelist
    }
    return render(request, 'disNinjas/ninjas.html', context)

def ninja(request, color):
    colorSelected = []
    if color == 'red':
        colorSelected.append('red.jpg')
    elif color =='blue':
        colorSelected.append('blue.jpg')
    elif color =='orange':
        colorSelected.append('orange.jpg')
    elif color =='purple':
        colorSelected.append('purple.jpg')
    else:
        colorSelected.append('notapril.jpg')

    context={
        'images':colorSelected
    }

    return render(request, 'disNinjas/ninjas.html', context)
