from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержания")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата содержания")
    status = models.BooleanField(default=True, verbose_name="Статус публикации")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    