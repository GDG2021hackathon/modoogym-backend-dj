from django.contrib import admin

from .models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "fitness", "price", "end_date", "seller", "buyer", "validation"]


admin.site.register(Membership, MembershipAdmin)
