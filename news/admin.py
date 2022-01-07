from django.contrib import admin

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at")
    fields = ("title", "description")
    readonly_fields = ("created_at", )
    search_fields = ("title", )

