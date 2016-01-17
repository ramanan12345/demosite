from django.contrib import admin

from .models import ArticlePage, ArticleCategory

admin.site.register(ArticlePage)

class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }

admin.site.register(ArticleCategory, ArticleCategoryAdmin)