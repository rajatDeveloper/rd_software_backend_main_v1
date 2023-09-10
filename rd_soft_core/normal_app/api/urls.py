from django.urls import path , include 
from .views import data_list
# from rest_framework.routers import DefaultRouter
from normal_app.api.views  import ContactUsView  , FeedBackView , ClientView , ProjectView


urlpatterns = [
    #test end point 
    path('test', data_list , name='test'),
    # get contact list and post contact end point 
    path('contact_us', ContactUsView.as_view() , name='contact_us'),
    # get contact list and post contact end point 
    path('feedback', FeedBackView.as_view() , name='feedback'),
    # get clinet list and post end point 
    path('client', ClientView.as_view() , name='client'),
    # get clinet list and post end point 
    path('project', ProjectView.as_view() , name='project'),    
        
]


