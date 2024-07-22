from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:cat_slug>/', views.catalog_slug, name='helicopter_slug'),
    path('login/', views.login, name='login'),
]