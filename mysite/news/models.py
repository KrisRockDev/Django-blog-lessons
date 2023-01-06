from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) # blank=True поле не обязательно для заполнения
    created_at = models.DateTimeField(auto_now_add=True) # поле заполняет дату и время в момент создания
    updated_at = models.DateTimeField(auto_now=True) # поле заполняется при изменении новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
