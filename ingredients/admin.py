from django.contrib import admin

from ingredients.models import Ingredient, Category

admin.site.register([Ingredient, Category])