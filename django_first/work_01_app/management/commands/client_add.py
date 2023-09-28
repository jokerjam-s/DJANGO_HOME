from django.core.management.base import BaseCommand
from work_01_app.models import Client


class Command(BaseCommand):
    help = "Добавление нового клиента."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='ФИО клиента')
        parser.add_argument('email', type=str, help='Email клиента')
        parser.add_argument('password', type=str, help='Пароль')
        parser.add_argument('-p', '--phone', type=str, help='Телефон')
        parser.add_argument('-a', '--address', type=str, help='Адрес')

    def handle(self, *args, **options):
        client_name = options.get('name')
        email = options.get('email')
        password = options.get('password')
        phone = options.get('phone')
        address = options.get('address')

        client = Client(client_name=client_name, email=email, password=password, phone=phone, address=address)
        client.save()
        self.stdout.write(f'{client}')
