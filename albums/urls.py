from django.urls import path

from .views import get_album

urlpatterns = [
    path('albums/', get_album)
]
