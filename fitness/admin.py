from django.contrib import admin

from .models import Fitness


class FitnessAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "location"]


admin.site.register(Fitness, FitnessAdmin)
