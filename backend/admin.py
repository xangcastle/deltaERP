from django.contrib import admin
from .forms import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name')
    list_filter = ('active',)
    search_fields = ('code', 'name')


@admin.register(Journal)
class JournalAdmin(ImportExportModelAdmin):
    pass


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

