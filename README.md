# Фреймворк Django

**Содержание**

[Первое Знакомство с Django](#первое-знакомство-с-django)<br>
[Django ORM и связи](#django-orm-и-связи)

## Первое Знакомство с Django

Создайте пару представлений в вашем первом приложении:
- главная
- о себе.

Внутри каждого представления должна быть переменная html — многострочный текст с 
HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.

Сохраняйте в логи данные о посещении страниц.

**Пример выполнения**

![img.png](img_readme/img_01.png)

![img.png](img_readme/img_02.png)

![img.png](img_readme/img_03.png)

## Django ORM и связи

Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
- имя клиента
- электронная почта клиента
- номер телефона клиента
- адрес клиента
- дата регистрации клиента

Поля модели «Товар»:
- название товара
- описание товара
- цена товара
- количество товара
- дата добавления товара

Поля модели «Заказ»:
- связь с моделью «Клиент», указывает на клиента, сделавшего заказ
- связь с моделью «Товар», указывает на товары, входящие в заказ
- общая сумма заказа
- дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально.

 