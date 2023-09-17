from rest_framework import serializers
from normal_app.models import ContactUs , FeedBack , Client  ,ProjectModel

class ConatctUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactUs
        fields = '__all__'
        
class FeedBackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FeedBack
        fields = '__all__'      
        
class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'           
        
class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectModel
        fields = '__all__'                   
        
        
        
        