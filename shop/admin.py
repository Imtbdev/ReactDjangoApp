from django.contrib import admin
from .models import Product, Category, Colors, Gender, Size, CustomUser, Manufacturer, SubCategory

admin.site.register(Colors)
admin.site.register(Gender)
admin.site.register(Size)
admin.site.register(Manufacturer)
admin.site.register(SubCategory)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ['content', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ['size', 'color', 'gender']
    list_filter = ["size", 'gender', 'category', 'sub_category']
    list_display = ['name', 'unique_id', 'sub_category', 'manufacturer', 'price', 'quantity']

    readonly_fields = ('img_preview', 'popularity_counter')
