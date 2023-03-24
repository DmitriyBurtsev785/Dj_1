from django.contrib import admin

# Register your models here.

from .models import Product

admin.site.register(Product) # нужно её здесь зарегистрировать, указываем название модели - (Product)