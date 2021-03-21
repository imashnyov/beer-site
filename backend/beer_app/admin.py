from django.contrib import admin
from .models import Beer

# Register your models here.
@admin.register(Beer)
class PostAdmin(admin.ModelAdmin):
    list_filter = (
        'mark',
        'price',
        'created',
    )
    search_fields = ('name',)
    date_hierarchy = 'created'

