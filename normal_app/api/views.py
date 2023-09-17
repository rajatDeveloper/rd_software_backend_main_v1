from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from normal_app.models import ContactUs , FeedBack , Client , ProjectModel
from normal_app.api.serializers import ConatctUsSerializer , FeedBackSerializer , ClientSerializer , ProjectSerializer
# # Create your views here.


#contact us view with get list of contacts and post -> 

class ContactUsView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ConatctUsSerializer
    
#feedback view with get list of contacts and post -> 

class FeedBackView(generics.ListCreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer   


#feedback view with get list of contacts and post -> 

class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  


class ProjectView(generics.ListCreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer 

def data_list(request):
    return JsonResponse({'server':"server is up !"})
