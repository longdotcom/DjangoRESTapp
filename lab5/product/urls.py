from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'product'
urlpatterns = [
    path('', TemplateView.as_view(template_name='product/index.html'), name='load' ),
    path('get/', views.getproducts, name='getproducts'),
    path('add/', views.addproduct, name='addproduct' ),
    path('delete/', views.deleteproduct, name='deleteproduct'),

    #path('deleteproduct/<prod_id:int>', views.deleteproduct, name='deleteproduct'),
    path('update/', views.updateproduct, name='updateproduct'),
]
