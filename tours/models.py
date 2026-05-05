from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя человека")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

class Horse(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка коня")
    # One To One - 1 человек может взять себе только 1 коня
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="horse", verbose_name="Владелец")

    def __str__(self):
        return f"Конь {self.name} (Владелец: {self.owner.name})"

    class Meta:
        verbose_name = "Конь"
        verbose_name_plural = "Кони"

class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название услуги")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class TourCompany(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    # ManyToMany - у одной компании много услуг и у одной услуги много компаний
    services = models.ManyToManyField(Service, related_name="companies", verbose_name="Услуги")

    def __str__(self):
        return self.name

    def get_average_rating(self):
        # Доп ДЗ: Вычислить средний рейтинг тур компании
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        if avg is not None:
            return round(avg, 1)
        return 0

    class Meta:
        verbose_name = "Тур. компания"
        verbose_name_plural = "Тур. компании"

class Review(models.Model):
    # One To Many - 1 человек может отставить несколько отзывов
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="reviews", verbose_name="Автор отзыва")
    company = models.ForeignKey(TourCompany, on_delete=models.CASCADE, related_name="reviews", verbose_name="Компания")
    text = models.TextField(verbose_name="Текст отзыва")
    
    # Доп Дз - оценки от 1 до 5
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Оценка может быть только от 1 до 5"),
            MaxValueValidator(5, message="Оценка может быть только от 1 до 5")
        ],
        verbose_name="Оценка"
    )

    def __str__(self):
        return f"Отзыв от {self.author.name} на {self.company.name} ({self.rating}/5)"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
