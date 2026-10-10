a simple project of watchstore

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
