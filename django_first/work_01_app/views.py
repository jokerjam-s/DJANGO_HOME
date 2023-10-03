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
    context = {'clients': clients}
    return render(request, 'work_01_app/clients_list.html', context)


def client_orders(request, client_id):
    """Отображение заказов пользователя."""
    client = get_object_or_404(Client, pk=client_id)
    # orders = Order.objects.prefetch_related('products').select_related('order_prods').filter(client_id=client_id)

    order_prods = OrderProducts.objects.select_related('product').select_related('order').filter(
        order__client_id=client_id).order_by('-order_id', )

    context = {
        'client': client,
        'orders': order_prods,
    }

    return render(request, 'work_01_app/client_orders.html', context)
