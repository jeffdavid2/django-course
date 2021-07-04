from django.contrib import admin
from django.urls import path
from .views import home, contact, about, login , products

urlpatterns = [
    path('/products', products, name="products"),
    path('/login', login, name='login'),
    path('/about', about, name='about'),
    path('/contacto', contact, name="contact"),
    path('/', home, name="home"),

]
