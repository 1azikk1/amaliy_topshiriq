from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Mahsulot Turi')
    is_available = models.BooleanField(default=True, verbose_name="Bor yoki Yo'q")

    class Meta:
        verbose_name = 'Tur '
        verbose_name_plural = 'Turlar'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='nomi')
    price = models.IntegerField(default=0, verbose_name='narxi')
    about = models.TextField(verbose_name='haqida')
    photo = models.ImageField(upload_to="products/photos", default='https://www.google.com/url?sa=i&url=https%3A%2F%2Folmamarket.uz%2Fuz&psig=AOvVaw1UjUk3nDasxRTmkn4Ql8J4&ust=1734696416461000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMDP_fDls4oDFQAAAAAdAAAAABAE')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='qoshilgan vaqti')
    quantity = models.IntegerField(verbose_name='miqdori')
    is_available = models.BooleanField(verbose_name='mavjud yoki yoq')
    comment = models.TextField(null=True, blank=True, verbose_name='izoh')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='mahsulot turi')

    class Meta:
        verbose_name = 'Mahsulot '
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return self.name
