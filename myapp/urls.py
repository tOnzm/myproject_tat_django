from django.urls import path
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete),
    


   
]