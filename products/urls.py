from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view(),name='product-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('luxury-special/', LuxurySpecialListView.as_view(), name='luxury-special-list'),
    path('me/wishlist/', MyWishListView.as_view(), name='my-wishlist')
]
