from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template import loader

def upGambar(request):

    return HttpResponse('hello world')