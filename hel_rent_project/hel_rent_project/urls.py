from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helicopter.urls')),
]

handler404 = page_not_found  # обработчик ошибки 404

admin.site.site_header = "Панель администрирования"  # заголовок в панели администратора
admin.site.index_title = "Аренда вертолетов"  # заголовок в панели администратора