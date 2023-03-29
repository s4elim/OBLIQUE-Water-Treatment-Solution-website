from django.contrib import admin

from ObliqueApp.models import Blog,Services,About

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','create_at','updated_at')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title','create_at','updated_at')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','create_at','updated_at')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Services)
admin.site.register(About)