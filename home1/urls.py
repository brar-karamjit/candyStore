from django.contrib import admin
from django.urls import path, include
from home1 import views

urlpatterns = [
    path('', views.index, name='home1'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('sub', views.sub, name='sub'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('assort', views.assort, name='assort')
]