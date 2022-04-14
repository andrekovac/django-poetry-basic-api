from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def get_album(request):
    return JsonResponse({"name": "Beat it!", "artist": "Michael Jackson"})
