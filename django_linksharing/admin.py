from django.contrib import admin
from models import Link

class LinkAdmin(admin.ModelAdmin):
    list_per_page = 25
    save_on_top = True
    list_display = ('url', 'description', 'author')
    search_fields = ('url', 'description')

    def save_form(self, request, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.author = request.user
        return instance
admin.site.register(Link, LinkAdmin)
