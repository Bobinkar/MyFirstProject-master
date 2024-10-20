from django.contrib import admin

from .models import Article
from .models import Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user',)
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
