from django.contrib import admin

from .models import Fitness


class FitnessAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Fitness, FitnessAdmin)
