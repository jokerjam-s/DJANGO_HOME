from django.db import models
from django.core.validators import MinValueValidator


class Client(models.Model):
    """Клиент интернет магазина."""
    client_name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)
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
    description = models.TextField(null=True, default=None)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    prod_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    append_date = models.DateTimeField(auto_now=True)  # фиксируем последнее изменение
    photo = models.ImageField(upload_to='media/', null=True, default=None)

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
    products = models.ManyToManyField(Product, through='OrderProducts')

    def __str__(self):
        return f'{self.pk} - {self.order_date}'


class OrderProducts(models.Model):
    """Количественный состав заказа по продуктам."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_count = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.order.primary_key}. {self.product.name} - {self.product_count}'
