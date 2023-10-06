from datetime import date, timedelta

from django.db.models import Sum, F

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
    """Отображение заказов пользователя.

    :client_id: код клиента, по которому проводится выборка
    """
    client = get_object_or_404(Client, pk=client_id)
    # orders = Order.objects.prefetch_related('products').select_related('order_prods').filter(client_id=client_id)

    order_prods = OrderProducts.objects.select_related('product').select_related('order').filter(
        order__client_id=client_id).order_by('-order_id')

    order_prods = order_prods.annotate(prod_cost=F('product__price') * F('product_count'))

    context = {
        'client_name': client.client_name,
        'orders': order_prods,
    }

    return render(request, 'work_01_app/client_orders.html', context)


def client_prods(request, client_id, days_history):
    """
    Список товаров заказанных клиентом за определенное кол-во дней.

    :client_id: клиент по которому проводится выборка
    :days_history: кол-во дней, за которые проводится просмотр истории
    """
    client = get_object_or_404(Client, pk=client_id)
    date_start = date.today() - timedelta(days=days_history)

    prod_info = OrderProducts.objects.select_related('product').select_related('odrders').filter(
        order__order_date__gte=date_start, order__client_id=client_id)
    prod_info = prod_info.values('product__prod_name', 'product__price').annotate(count_prod=Sum('product_count'))
    prod_info = prod_info.annotate(cost=F('product__price') * F('count_prod'))

    context = {
        'client_name': client.client_name,
        'period': period(days_history),
        'products': prod_info
    }

    return render(request, 'work_01_app/client_products.html', context)


def period(days: int) -> str:
    """Период отчетности."""
    match days:
        case 7:
            return 'за последнюю неделю'
        case 30:
            return 'за последний месяц'
        case 365:
            return 'за последний год'
    return 'за произвольный период'


def products_list(request):
    """Отображение списка продуктов."""
    products = Product.objects.all()

    show_no_del = False

    context = {
        "products": products,
        "show_no_del": show_no_del,
    }

    return render(request, "work_01_app/products_list.html", context)
