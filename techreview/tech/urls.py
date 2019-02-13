from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('techtypes/', views.techtypes, name='techtypes'),
    path('products/', views.getproducts, name='getproducts'),
    path('productdetail/<int:id>', views.productdetail, name='details')
]