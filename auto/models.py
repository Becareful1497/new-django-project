from django.db import models

class CategoryCar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category car"
        verbose_name_plural = "Category cars"

class Car(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryCar, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

class NummerCar(models.Model):
    number = models.CharField(max_length=20)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Nummer car"
        verbose_name_plural = "Nummer cars"

class ReviewCar(models.Model):
    text = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.car}"

    class Meta:
        verbose_name = "Review car"
        verbose_name_plural = "Review cars"
