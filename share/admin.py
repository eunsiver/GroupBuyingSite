from django.contrib import admin
# Register your models here.
from.models import Post,Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
