import datetime 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def index(request):
    context={"tags" : [
    { 'tag': 'gstreamer_cctv_streaming', 'size': 10 },
    { 'tag': 'microk8s_with_2_rpis', 'size': 8 },
    { 'tag': 'docker', 'size': 1 },
    { 'tag': 'git', 'size': 6 },
    { 'tag': 'regex', 'size': 3 },
    { 'tag': 'rest_api', 'size': 9 },
    { 'tag': 'why_http_2', 'size': 7 },
    { 'tag': 'graphana', 'size': 5 },
    { 'tag': 'bigpipe', 'size': 2 },
    { 'tag': 'telnet', 'size': 4 },
],}
    return render(request,'index.html',context)
def home(request):
    return render(request,'home.html')