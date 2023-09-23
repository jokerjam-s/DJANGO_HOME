from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница."""
    html = ("<a href='/'>Home</a>&nbsp;&nbsp;"
            "<a href='/about/'>About</a>"
            "<h1>Hello, guest!</h1>"
            "<p>This is my first Django project.</p>"
            "<p>If you can see this text - I'm on the right way!</p>"
            )
    return HttpResponse(html)


def about(request):
    """Страница About."""
    html = ("<a href='/'>Home</a>&nbsp;&nbsp;"
            "<a href='/about/'>About</a>"
            "<h1>About me.</h2>"
            "<h3>Hello! I'm Andrey.</h3>"
            "<p>This html page is part of my first django application.</p>"
            "<p>I'm learning python development.</p>"
            )
    return HttpResponse(html)
