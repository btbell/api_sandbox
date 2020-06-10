from django.contrib import admin
from . import models

@admin.register(models.MediaMention)
class MediaMentionAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'title', 'category', 'publication_date',)
