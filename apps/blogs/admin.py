from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
