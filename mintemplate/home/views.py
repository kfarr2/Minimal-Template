import os, sys
from django.shortcuts import render

def home(request):
    """ Default Home View """
    return render(request, 'home/home.html', {
        
    })
