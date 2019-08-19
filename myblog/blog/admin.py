from django.contrib import admin
from django.utils import timezone
from blog.models import Post, Blog, Comment, Author

class PostInLine(admin.StackedInline):
    model = Post
    extra = 3

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ['name', 'tagline']
    inlines = [PostInLine]
    list_display = ('name', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['author_nickname', 'text', 'in_post']
    list_display = ('author_nickname', 'in_post', 'date_publish')
    list_filter = ['date_publish', 'author_nickname']

@admin.register(Post)    
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title', 'text']}),
        ("Info about post", {"fields": ['authors', 'in_blog']}),
        ("Info about publication", {"fields": ['is_published', 'date_publish']}),
    ]
    list_display = ('title', 'date_publish', 'is_published')
    list_filter = ['date_publish']
    actions = ['publicate_posts']

    def publicate_posts(self, request, queryset):
        queryset.update(date_publish=timezone.now(), is_published=True)
    publicate_posts.short_description = 'Publicate posts'

admin.site.register(Author) 