from django.contrib import admin
from .models import Person, Horse, Service, TourCompany, Review

admin.site.register(Person)
admin.site.register(Horse)
admin.site.register(Service)

@admin.register(TourCompany)
class TourCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_average_rating_display')
    filter_horizontal = ('services',)

    def get_average_rating_display(self, obj):
        return f"{obj.get_average_rating()} / 5"
    get_average_rating_display.short_description = "Средняя оценка"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('company', 'author', 'rating')
    list_filter = ('rating', 'company')
