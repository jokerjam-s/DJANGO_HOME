from django.core.management.base import BaseCommand
from work_01_app.models import Client


class Command(BaseCommand):
    help = "Изменение клиента"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help='Идентификатор клиента')
        parser.add_argument('-n', '--name', type=str, help='ФИО клиента')
        parser.add_argument('-e', '--email', type=str, help='Email клиента')
        parser.add_argument('-pwd', '--password', type=str, help='Пароль')
        parser.add_argument('-p', '--phone', type=str, help='Телефон')
        parser.add_argument('-a', '--address', type=str, help='Адрес')

    def handle(self, *args, **options):
        pk = options['pk']
        client_name = options['name']
        email = options['email']
        password = options['password']
        phone = options['phone']
        address = options['address']

        client = Client.objects.filter(pk=pk).first()

        if client:
            if client_name is not None:
                client.client_name = client_name
            if email is not None:
                client.email = email
            if password is not None:
                client.password = password
            if phone is not None:
                client.phone = phone
            if address is not None:
                client.address = address

            client.save()

        self.stdout.write(f'{client}')
