from django.contrib import admin
from .models import Post, Author

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    fields = ('username', 'email', 'first_name', 'last_name')

class PostAdmin(admin.ModelAdmin):
    list_filter = ('edit_date', 'author')
    fields = ('title', 'author', 'body')
    list_display = ('title', 'author', 'edit_date', 'edit_time')


admin.site.register(Author, UserAdmin)
admin.site.register(Post, PostAdmin)
