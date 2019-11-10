from django.contrib import admin

from blogs.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):

    fields = ['title','author','status','content']

    search_fields = ['title','status']

admin.site.register(Post, PostAdmin)