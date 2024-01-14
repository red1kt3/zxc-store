from django.urls import path
from apps.order import views


urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),
    path('add/', views.add_to_card, name='add_to_card'),
    path('create/', views.create_order, name='create_order'),
    path('remove/<int:row_id>', views.remove_from_cart, name='remove'),

]
