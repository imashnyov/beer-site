from django.contrib import admin
from .models import Beer, UserComment, UserMark


class UserMarkInline(admin.StackedInline):
    model = UserMark
    # fields = ('owner__email', 'mark')
    extra = 0


class UserCommentInline(admin.StackedInline):
    model = UserComment
    # fields = ('owner__email', 'test')
    extra = 0


@admin.register(Beer)
class PostAdmin(admin.ModelAdmin):
    list_filter = (
        'mark',
        'price',
        'created',
    )
    list_display = (
        'name',
        'mark',
        'created'
    )
    search_fields = ('name',)
    date_hierarchy = 'created'
    inlines = [UserMarkInline, UserCommentInline]
