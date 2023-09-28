from django.db import models
from django.core.validators import MinValueValidator


class Client(models.Model):
    """Клиент интернет магазина."""
    client_name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    reg_date = models.DateField(auto_now_add=True)  # фиксируем создание

    def __str__(self):
        return f'{self.client_name}, email. {self.email}'

    class Meta:
        """Организация вывода, индексы."""
        ordering = ['client_name']
        indexes = [
            models.Index(fields=['client_name']),
            models.Index(fields=['-reg_date']),
        ]


class Product(models.Model):
    """Товары, реализуемые в магазине."""
    prod_name = models.CharField(max_length=250, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    prod_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    append_date = models.DateTimeField(auto_now=True)  # фиксируем последнее изменение

    def __str__(self):
        return f'{self.prod_name}, наличие: {self.prod_count}, цена: {self.price}'

    class Meta:
        ordering = ['prod_name']
        indexes = [
            models.Index(fields=['prod_name']),
            models.Index(fields=['-append_date']),
            models.Index(fields=['price']),
        ]


class Order(models.Model):
    """Заказы клиентов магазина."""
    order_date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.pk} - {self.order_date}'
