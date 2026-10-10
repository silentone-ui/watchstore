from rest_framework import serializers

from .models import Product,ProductImage,Comment,Wishlist

class ProductListSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name',read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id','title','slug','price','brand_name','category_name','is_available','stash']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields = ['image']

class CommentSerializer(serializers.ModelSerializer):
    customer_name =serializers.CharField(source='customer.user.username',read_only=True)   
    class Meta:
        model=Comment
        fields = ['customer_name','body','created_at']

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    colors = serializers.StringRelatedField(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    category_name = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model=Product
        fields = ['id','title','slug','price','description','main_image','brand','brand_name',
                'category','category_name','is_discount','is_available','is_special','is_luxury',
                'gender','origin','strap_material','usage','design','engine',
                'features','stash','click_count','images','colors','comments',
                'created_at','updated_at']


class LuxurySpecialProductSerializer(serializers.ModelSerializer):
    avg_price = serializers.FloatField(read_only=True)

    class Meta:
        model=Product
        fields=['title','price','gender','strap_material','engine','avg_price']



class WishListSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title', read_only=True)
    product_slug = serializers.CharField(source='product.slug', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    product_stash = serializers.IntegerField(source='product.stash', read_only=True)
    product_main_image = serializers.ImageField(source='product.main_image', read_only=True)

    username = serializers.CharField(source='customer.user.username', read_only=True)
    email = serializers.EmailField(source='customer.user.email', read_only=True)
    phone_number = serializers.CharField(source='customer.phone_number', read_only=True)

    class Meta:
        model = Wishlist
        fields = [
            'id',
            'product_title', 'product_slug', 'product_price',
            'product_stash', 'product_main_image',
            'username', 'email', 'phone_number'
        ]