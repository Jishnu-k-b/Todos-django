from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "body",
        "title",
    )


admin.site.register(Todo, TodoAdmin)
