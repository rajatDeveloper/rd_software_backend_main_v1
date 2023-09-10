from django.shortcuts import render

from django.http import JsonResponse


# # Create your views here.
def data_list(request):
    return JsonResponse({'data':"data is here"})
