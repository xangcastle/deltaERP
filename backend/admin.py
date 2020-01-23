from django.contrib import admin
from .models import *


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    list_filter = ('active',)
    search_fields = ('code', 'name')


class DocumentJournals(admin.TabularInline):
    model = Journal
    extra = 0
    classes = ('grp-collapse', 'grp-open')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('number', 'date', 'concept')
    inlines = [DocumentJournals, ]
