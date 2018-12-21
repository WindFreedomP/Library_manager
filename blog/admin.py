from django.contrib import admin

from .models import BlogArticle
# Register your models here.
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author")
    list_filter=("author",)
    search_fields=("title","body")
    raw_id_fields=("author",)
admin.site.register(BlogArticle,BlogArticlesAdmin)
