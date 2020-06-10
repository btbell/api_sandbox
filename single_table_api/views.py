from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MediaMentionSerializer
from .models import MediaMention

def home(request):
    return HttpResponse('home')

