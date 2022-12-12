from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'