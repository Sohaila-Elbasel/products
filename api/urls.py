from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('category/', views.category, name='category'),
    path('category/<int:id>/', views.edit_category, name='edit_category'),
    path('product/', views.product, name='products'),
    path('product/<int:id>/', views.edit_product, name='edit_products'),

]
