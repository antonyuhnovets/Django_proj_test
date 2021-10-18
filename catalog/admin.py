from django.contrib import admin
from .models import Post, Author

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    fields = ('username', 'name', 'email', 'date_of_birth')

class PostAdmin(admin.ModelAdmin):
    list_filter = ('edit_date', 'author')
    fields = ('title', 'author', 'body')
    list_display = ('title', 'author', 'edit_date', 'edit_time')


admin.site.register(Author, UserAdmin)
admin.site.register(Post, PostAdmin)
