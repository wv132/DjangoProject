from django.contrib import admin
from .models import Issue
# Register your models here.

class IssueAdmin(admin.ModelAdmin):
    date_hierarchy = 'opened_on'
    list_filter = ('status', 'owner')
    list_display = ('id', 'title', 'summary', 'status','owner')
    search_fields = ['description', 'status']


admin.site.register(Issue,IssueAdmin)