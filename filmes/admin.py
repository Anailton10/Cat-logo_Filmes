from django.contrib import admin
from .models import FilmRegistration, Category


class FilmAdmin(admin.ModelAdmin):
    list_play = ('title', 'category', 'duration', 'author')
    search_fields = ('title', 'category')


admin.site.register(FilmRegistration, FilmAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)


admin.site.register(Category, CategoryAdmin)
