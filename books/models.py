from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=150, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    published_date = models.DateField(verbose_name="Дата публикации")
    isbn = models.CharField(max_length=20, verbose_name="ISBN")
    pages = models.IntegerField(verbose_name="Количество страниц")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    language = models.CharField(max_length=50, verbose_name="Язык")
    publisher = models.CharField(max_length=150, verbose_name="Издательство")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
