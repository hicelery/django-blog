from django.contrib import admin
from about.models import AboutPage, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(AboutPage)


@admin.register(AboutPage)
class AboutPageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'updated_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
