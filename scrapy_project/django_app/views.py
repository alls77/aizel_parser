import redis

from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib import messages

from django_app.models import Product


class IndexView(TemplateView):
    template_name = 'django_app/index.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def post(self, request):
        self.redis.lpush('aizel:start_urls', 'https://aizel.ru/ua-ru/zhenskoe/obuv')
        messages.info(request, 'Parser started, after the end a link will appear.')
        return render(request, self.template_name)


class ProductsView(ListView):
    template_name = 'django_app/products.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.prefetch_related('images', 'sizes').select_related('brand', 'category', 'price')

