from django.contrib import admin

# Register your models here.
from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created',)
