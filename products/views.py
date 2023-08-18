from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from products.models import ProductCategory, Product, Basket
from common.views import TitleMixin

from django.core.cache import cache

class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store-продукты'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        # Кеширование
        # categories = cache.get('categories')
        # if not categories:
        #     context['categories'] = ProductCategory.objects.all()
        #     cache.set('categories', context['categories'], 30)
        # else:
        #     context['categories'] = categories
        return context

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# def products(request, category_id=None, page_namber=1):
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#
#     per_page = 3
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_namber)
#
#     context = {
#         'title':'Store-продукты',
#         'products': products_paginator,
#         'categories': ProductCategory.objects.all(),
#     }
#
#     return render(request, 'products/products.html', context)
