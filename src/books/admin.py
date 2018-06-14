from django.contrib import admin

# Register your models here.
from books.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    date_hierarchy = 'publication_date'
    ordering = ['-publication_date']
    fields = ('title','publisher','author','publication_date')
    filter_vertical = ('author',)
    raw_id_fields = ('publisher',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)