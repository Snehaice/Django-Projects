from django.contrib import admin
from base.models import categories,articles

# Register your models here.
admin.site.register(categories),

class articlesAdmin(admin.ModelAdmin):
    list_display=['title','category','created_at','status','is_trending']
    prepopulated_fields={'slug':('title',)}

admin.site.register(articles,articlesAdmin),
    