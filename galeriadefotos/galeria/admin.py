from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'date_taken', 'created_at']
    list_filter = ['location', 'date_taken', 'created_at']
    search_fields = ['title', 'location', 'description']
    readonly_fields = ['created_at']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'location', 'date_taken')
        }),
        ('Descrição', {
            'fields': ('description',)
        }),
        ('Imagem', {
            'fields': ('image',)
        }),
        ('Metadados', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
