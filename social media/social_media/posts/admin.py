from django.contrib import admin
from .models import Post, Comment, Vote



# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created", "is_reply")
    raw_id_fields = ('user', 'post', 'reply')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Vote)
