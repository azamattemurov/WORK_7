from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryModels(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductsModels(models.Model):
    objects = None
    category = models.ForeignKey(CategoryModels, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    info = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    retyting = models.IntegerField()
    discount = models.IntegerField()
    brand = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_discount(self):
        return self.discount != 0

    def is_available(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.discount * self.price / 100

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class FaqModel(models.Model):
    objects = None
    question = models.CharField(max_length=500, verbose_name=_('question'))
    answer = models.CharField(max_length=500, verbose_name=_('answer'))

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.question)

    class Meta:
        verbose_name = _('Faq')
        verbose_name_plural = _('Faqs')



