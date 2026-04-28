

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена (UZS)")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    expire_date = models.DateField(verbose_name="Срок годности")
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="Кол-во")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Итого")
    date = models.DateTimeField(auto_now_add=True)