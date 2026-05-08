from django.contrib import admin

from app.models import Category, Post

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'author', 'created_at', 'published_at')
    list_editable = ['status']
    list_filter = ('status', 'created_at', 'category')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at', 'published_at')
    date_hierarchy = 'created_at'




