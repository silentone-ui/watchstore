from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class SluggedMixinModel(models.Model):
    slug = models.SlugField(unique=True,max_length=255)

    class Meta:
        abstract = True