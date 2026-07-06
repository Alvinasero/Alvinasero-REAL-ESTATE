from django.urls import path

from . import views


urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('listings/', views.property_list, name='property_listings'),
    path('detail/', views.property_detail, name='property_detail'),
    path('manage/', views.manage_properties, name='manage_properties'),
    path('add/', views.add_property, name='add_property'),
    path('edit/', views.edit_property, name='edit_property'),
]
