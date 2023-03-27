from django.db import models

# Create your models here.


# class Product(models.Model): # наследуется от класса models.Model, аналог класса Base в SQLAlchemy.
#     # Все свойства, которые будут у этого объекта, я должен описать вот в таком виде"""
#     name = models.CharField(max_length=50) # имя товара будет наименование какое-то. За это отвечает поле CharField
#     # Когда использую CharField нужно указывать максимаьную длину (max_length=50)"""
#     description = models.CharField() # это у нас будет текст, ограничение кода нет
#     color = models.CharField(max_length=20 )# у товара пусть будет цвет
#     price = models.DecimalField(max_digits=10, decimal_places=2) # пусть будет цена
#     # Когда DecimalField используем, нужно указать два свойства: кол-во цифр (max_digits=10)
#     # и сколько будет после запятой (decimal_places=2)"""
#     image = models.ImageField(upload_to='products/')# сделаем так, чтобы можно было какое-нибудь изображение привязать
#     # upload_to='images/'   -  нужно указать в какую папку загружать картинки"""
#
#     # Когда задаём классы, не забываем задавать метод __str__"""
#     def __str__(self): # строчное представление объекта
#     # """Нужен для того, чтобы объекты между собой различать, когда мы выводим объекты в консоль,
#     # объекты выводятся в следующем виде <Class> object at 98566776556778
#     # Два товара будут различаться только тем, что у них будет разные адреса в памяти -98566776556778
#     # По этим адресам не понятно где какой товар
#     # Чтобы они отображались каким-то понятным образом, чтобы понимали, где какой объект, задаю этот метод"""
#         return self.name # обычно подают название (или что-то другое, что позволит идентифицировать объект)
#         # то, что возвращаем, должно быть строкой, иначе будет ошибка

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


    def __repr__(self):
        return self.name