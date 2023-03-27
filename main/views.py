from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Product

# Create your views here.
def sample_controller(request):
    return HttpResponse("Hello world!")


def products_list(request):
    products = Product.objects.all()
    return render(request, 'main/list.html', {'products': products}) # вызываем функцию render
    # 1-м аргументом принимает request
    # 2 -м название шаблона в виде пути в кавычках, от папки templates
    # в качестве данных нам нужно отдать товары products
    # данные передаются в виде словаря, в качестве ключа мошу задать всё, что угодно
    # в кач-ве значения, то, что хочу передать, т.е. сами данные)
