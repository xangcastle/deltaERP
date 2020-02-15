from django.contrib import admin
from .forms import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'total_debit', 'total_credit')
    list_filter = ('active',)
    search_fields = ('code', 'name')


@admin.register(Journal)
class JournalAdmin(ImportExportModelAdmin):
    list_display = ('debit', 'credit', 'date', 'number', 'concept')
    list_filter = ('account', )
    search_fields = ('document__number', 'document__concept')


class DocumentJournals(admin.TabularInline):
    model = Journal
    extra = 0
    classes = ('grp-collapse', 'grp-open')


@admin.register(Document)
class DocumentAdmin(ImportExportModelAdmin):
    date_hierarchy = 'date'
    list_display = ('number', 'date', 'concept')
    inlines = [DocumentJournals, ]
    form = DocumentForm
    search_fields = ('number', 'concept')
    fieldsets = (
        ('', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('date', 'number', 'user'),
                ('concept',),
                ('debit_sum', 'credit_sum', 'difference'),
            )
        }),
    )

    class Media:
        js = ('backend/js/document.admin.js', )

