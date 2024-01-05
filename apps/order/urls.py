from django.urls import path
from apps.order import views


urlpatterns = [
    path('add/cart_view', views.cart_view, name='cart_view'),
    path('add/', views.add_to_card, name='add_to_card'),

]
