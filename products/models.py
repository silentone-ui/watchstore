from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel, SluggedMixinModel

GENDER_CHOICES = (
    ('men', 'مردانه'),
    ('women', 'زنانه'),
    ('unisex', 'اسپرت/مشترک')
)

class Brand(BaseModel):
    name = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Category(BaseModel, SluggedMixinModel):
    name = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
    def __str__(self):
        return self.name

class Product(BaseModel, SluggedMixinModel):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name='توضیحات کامل')
    main_image = models.ImageField(upload_to='products/', verbose_name='تصویر اصلی')

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    is_discount = models.BooleanField(default=False, verbose_name='دارای تخفیف')
    is_available = models.BooleanField(default=True, verbose_name='موجود است')
    is_special = models.BooleanField(default=False, verbose_name='محصول خاص')
    is_luxury = models.BooleanField(default=False, verbose_name='محصول لوکس')

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unisex')
    origin = models.CharField(max_length=100, help_text="کشور سازنده")
    strap_material = models.CharField(max_length=100, verbose_name="جنس بند")
    usage = models.CharField(max_length=100, verbose_name="کاربری")
    design = models.CharField(max_length=100, verbose_name="طراحی")
    engine = models.CharField(max_length=100, verbose_name="موتور")

    features = models.JSONField(blank=True, null=True, verbose_name='ویژگی ها (json)')
    stash = models.PositiveIntegerField(default=0, verbose_name='موجودی انبار')
    click_count = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')

    Meta_title = models.CharField(max_length=255, blank=True, null=True)
    Meta_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"

class Comment(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments', verbose_name="مشتری")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name="محصول")
    body = models.TextField(verbose_name="متن نظر")

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

class Wishlist(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='wishlist', verbose_name="مشتری")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist', verbose_name="محصول")

    class Meta:
        unique_together = ('customer', 'product')
        verbose_name = "علاقمندی"
        verbose_name_plural = "علاقمندی‌ها"

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/', verbose_name='تصویر')

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصول'

class ProductColor(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')
    color = models.CharField(max_length=50, verbose_name='رنگ')
    hex_code = models.CharField(max_length=7, verbose_name='کد رنگ')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'رنگ های محصول'
    



