from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_en, name='home_en'),
    path('bn/', views.home_bn, name='home_bn'),
    
    path('subjects/', views.subjects_en, name='subjects_en'),
    path('resources/', views.resources_en, name='resources_en'),
    
    # ADD THESE TWO NEW BANGLA URLS:
    path('bn/subjects/', views.subjects_bn, name='subjects_bn'),
    path('bn/resources/', views.resources_bn, name='resources_bn'),
]