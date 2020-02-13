from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app.getImageUrl import get_img_url


def index(request):

    return render(request, 'search.html')


def search_av(request):
    av_id = request.GET.get('av_id')
    data = get_img_url(av_id)
    return JsonResponse(data)
