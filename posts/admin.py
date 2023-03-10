from django.contrib import admin
from posts.models import  Post
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_filter = ["status"]
    list_editable = ["status"]


