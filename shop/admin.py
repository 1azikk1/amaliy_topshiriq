from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_available')
    list_display_links = ('id',)
    list_editable = ('name',)
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Category, AdminCategory)


class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'quantity', 'is_available', 'category', 'comment', 'get_photo')
    list_display_links = ('id', 'name')
    list_editable = ('quantity', 'is_available', 'category')
    actions_on_top = False
    actions_on_bottom = True

    def get_photo(self, product):
        if product.photo:
            return mark_safe(f'<img src="{product.photo.url}" width="200px">')
        return 'Rasm topilmadi!'


admin.site.register(Product, AdminProduct)
