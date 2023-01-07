from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'is_published',)
    list_display_links = ('id', 'title', ) # Добавляет ссылки на объект
    search_fields = ('title', 'content', ) # Добавляет поиск по содержимому полей

# Порядок регистрации важен, сначала регистрируется модель, потом её представление
admin.site.register(News, NewsAdmin)
