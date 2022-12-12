from . import views
from django.urls import path


urlpatterns = [
    path('',views.home),
    path('takepic',views.takepic_screen),
    path('camera',views.cameraopen),
    path('attendance',views.attendance),
    path('data',views.attendDataHtml),
    
    
    
    
]
