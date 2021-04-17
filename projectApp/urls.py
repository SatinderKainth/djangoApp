from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new',views.new),
    path('create',views.create),
    path('create/<int:number>',views.show),
    path('create/<int:number>/edit',views.edit),
    path('create/<int:number>/delete',views.destroy),
    
]