from work_01_app.models import Client, Order, Product, OrderProducts
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def index(request):
    """Главная страница."""
    return render(request, 'work_01_app/base.html')


def about(request):
    """Страница About."""
    return render(request, 'work_01_app/about.html')


def clients_list(request):
    """Список клиентов."""
    clients = Client.objects.all()
    content = {'clients': clients }
    return render(request, 'work_01_app/clients_list.html', content)


def client_orders(request, client_id):
    """Отображение заказов пользователя."""
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client_id)
    # orders_prod = [OrderProducts.objects.filter(order_id=order.pk) for order in orders]
    return HttpResponse(f'{orders[0].products}')