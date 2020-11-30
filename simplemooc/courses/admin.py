from django.contrib import admin

from .models import Course

class CouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date'] 
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# Aqui estamos registrando no painel do admin o Model do Course
admin.site.register(Course, CouseAdmin)
