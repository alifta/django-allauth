from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'user', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'created_at', 'updated_at')
    search_fields = ('description', 'user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_completed',)
