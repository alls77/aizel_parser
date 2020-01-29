from django.urls import path
from django_app import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.ProductsView.as_view(), name='products'),
]