from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'latitude', 'longitude', 'user', 'created_at')
    search_fields = ('description', 'user__username')
    list_filter = ('created_at', 'user')
