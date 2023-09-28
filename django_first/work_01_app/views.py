from django.shortcuts import render
from django.http import HttpResponse
from work_01_app.models import Client


def index(request):
    """Главная страница."""
    html = ("<a href='/'>Home</a>&nbsp;&nbsp;"
            "<a href='/about/'>About</a>&nbsp;&nbsp;"
            "<a href='/clients'>Clients</a>"
            "<h1>Hello, guest!</h1>"
            "<p>This is my first Django project.</p>"
            "<p>If you can see this text - I'm on the right way!</p>"
            )
    return HttpResponse(html)


def about(request):
    """Страница About."""
    html = ("<a href='/'>Home</a>&nbsp;&nbsp;"
            "<a href='/about/'>About</a>&nbsp;&nbsp;"
            "<a href='/clients'>Clients</a>"
            "<h1>About me.</h2>"
            "<h3>Hello! I'm Andrey.</h3>"
            "<p>This html page is part of my first django application.</p>"
            "<p>I'm learning python development.</p>"
            )
    return HttpResponse(html)


def clients_list(request):
    """Список клиентов."""
    clients = Client.objects.all()

    html = ("<a href='/'>Home</a>&nbsp;&nbsp;"
            "<a href='/about/'>About</a>&nbsp;&nbsp;"
            "<a href='/clients'>Clients</a>"
            "<h1>Clients list</h2>"
            "<table>"
            "<tr><td>Name</td><td>E-mail</td><td>Phone</td><td>Address</td></tr>"
            )
    for client in clients:
        html += ("<tr>"
                 f"<td>{client.client_name}</td>"
                 f"<td>{client.email}</td>"
                 f"<td>{client.phone}</td>"
                 f"<td>{client.address}</td>"
                 "</tr>")
    html += "</table>"
    return HttpResponse(html)
