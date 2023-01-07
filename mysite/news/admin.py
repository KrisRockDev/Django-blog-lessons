from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'content', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title', 'category',)  # Добавляет ссылки на объект
    search_fields = ('title', 'content',)  # Добавляет поиск по содержимому полей
    list_editable = ('is_published',)  # Изменять из админки
    list_filter = ('is_published', 'category',)  # Фильтр в админке


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)  # Добавляет ссылки на объект
    search_fields = ('title',)  # Добавляет поиск по содержимому полей


# Порядок регистрации важен, сначала регистрируется модель, потом её представление
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
