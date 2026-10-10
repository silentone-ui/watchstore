from rest_framework import generics,permissions
from .models import Product,Wishlist
from .serializers import ProductListSerializer,ProductDetailSerializer,LuxurySpecialProductSerializer,WishListSerializer
from django.db.models import F,Avg,Window


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return Product.objects.select_related('brand', 'category').all()


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Product.objects.select_related('brand','category').prefetch_related('images','colors','comments__customer__user'
        ).all()

    def get_object(self):
        obj = super().get_object()

        Product.objects.filter(pk=obj.pk).update(click_count=F('click_count') + 1)
        obj.refresh_from_db(fields=['click_count']) 
        return obj


class LuxurySpecialListView(generics.ListAPIView):
    serializer_class = LuxurySpecialProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(
            is_special=True,
            is_luxury=True,
            is_available=True,
        )

        return queryset.annotate(
            avg_price=Window(expression=Avg('price'))
        )

    

class MyWishListView(generics.ListAPIView):
    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.select_related(
            'product','customer__user'
        ).filter(customer__user=self.request.user)