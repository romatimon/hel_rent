from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from helicopter.forms import ApplicationForm
from helicopter.models import Helicopter


def index(request):
    return render(request, 'helicopter/index.html', {'title': 'Главная страница'})


def catalog(request):
    helicopters = Helicopter.objects.all()  # жадные запросы, загружаем все данные сразу

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')

    else:
        form = ApplicationForm()

    data = {
        'title': 'Каталог вертолетов',
        'helicopter_list': helicopters,
        'form': form
    }

    return render(request, 'helicopter/catalog.html', data)


def catalog_slug(request, cat_slug):
    starship = get_object_or_404(Helicopter, slug=cat_slug)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')

    else:
        form = ApplicationForm()

    data = {
        'title': starship.name,
        'helicopter': starship,
        'form': form
    }

    return render(request, 'helicopter/helicopter_slug.html', data)


def login(request):
    return redirect(catalog)


def page_not_found(request, exception):
    """Функция обработки ошибки 404 (страница не найдена)."""
    return HttpResponseNotFound('Страница не найдена. Ошибка 404. В будущем здесь будет редирект')