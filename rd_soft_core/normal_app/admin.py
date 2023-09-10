from django.contrib import admin
from normal_app.models import ContactUs , FeedBack , Client  , ProjectModel

# Register your models here.

admin.site.register(ContactUs, list_display=['id' , 'name' , 'email' , 'phone_number' ])

admin.site.register(FeedBack, list_display=['id' , 'name' , 'position' ,'company' ])

admin.site.register(Client, list_display=['id' , 'company_name'  ])

admin.site.register(ProjectModel, list_display=['id' , 'name' , 'link' , 'created_at'  ])



