from django.contrib import admin
from pages.models import ProductsModels, CategoryModels, FaqModel

# Register your models here.
admin.site.register(CategoryModels)
admin.site.register(ProductsModels)
admin.site.register(FaqModel)

