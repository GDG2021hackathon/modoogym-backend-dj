from django.contrib import admin

from .models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ["id", "fitness", "price", "user", "end_date"]



admin.site.register(Membership, MembershipAdmin)
