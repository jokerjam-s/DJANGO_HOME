from datetime import date, timedelta

from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, F
from django.shortcuts import render, get_object_or_404, redirect

from work_01_app.forms import ProductForm
from work_01_app.models import Client, Order, Product, OrderProducts


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
    # req_url = reverse('clients', args=(context, ))
    return render(request, 'work_01_app/clients_list.html', context=context)


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


def products_list(request, show_no_del: str = 'no'):
    """
    Отображение списка продуктов.

    :show_no_del: признак отображения сообщения.
    """
    products = Product.objects.all()

    context = {
        "products": products,
        "show_no_del": show_no_del,
    }

    return render(request, "work_01_app/products_list.html", context)


def product_delete(request):
    """
    Удаление товара. После завершения операции переходит в список товаров.
    В зависимости от результата возвращает параметр для отображения сообщения пользователю.
    """
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        prod = get_object_or_404(Product, pk=prod_id)

        if OrderProducts.objects.filter(product_id=prod.pk).exists():
            responce = redirect('products', 'yes')
        else:
            prod.delete()
            responce = redirect('products')
    else:
        responce = redirect('index')

    return responce


def product_create(request):
    """Запрос на создание нового товара."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)

            Product.objects.create(**form.cleaned_data)
            return redirect('products')
    else:
        form = ProductForm()

    return render(request, 'work_01_app/product_create.html', {'title': 'Новый товар', 'form': form})


def product_edit(request, prod_id: int = None):
    """Редактирование товара."""
    prod = get_object_or_404(Product, pk=prod_id)
    if request.method == 'GET':
        form = ProductForm(instance=prod)
        context = {
            'title': 'Изменить товар',
            "prod_id": prod_id,
            "form": form,
        }
        return render(request, 'work_01_app/product_create.html', context)
    else:
        form = ProductForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            form.save()

    return redirect('products')


def product_info(request, prod_id: int):
    """Информация о товаре."""
    prod = get_object_or_404(Product, pk=prod_id)

    return render(request, 'work_01_app/product_info.html', {'prod': prod})
