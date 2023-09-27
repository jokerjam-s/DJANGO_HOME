from django.core.management.base import BaseCommand
from django_first.work_01_app.models import Client

class Command(BaseCommand):
    help = "Добавление нового клиента."


    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='ФИО клиента')
        parser.add_argument('email', type=str, help='Email клиента')
        parser.add_argument('password', type=str, help='Пароль')
        parser.add_argument('phone', type=str, help='Телефон')
        parser.add_argument('address', type=str, help='Адрес')

    def handle(self, *args, **options):
        # todo: continue here
        # client = Client(client_name=args['name'], email=args['email'])
