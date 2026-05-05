from django.contrib import admin
from .models import Car, CategoryCar, NummerCar, ReviewCar

admin.site.register(Car)
admin.site.register(CategoryCar)
admin.site.register(NummerCar)
admin.site.register(ReviewCar)
