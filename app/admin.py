from django.contrib import admin

from .models import *
# Register your models here.

class FormationAdmin(admin.ModelAdmin):

    list_display = ['name', 'start_at', 'end_at', 'description']
admin.site.register(Formations, FormationAdmin)

class ExperienceAdmin(admin.ModelAdmin):

    list_display = ['type', 'post', 'start_at', 'end_at', 'etablisment_name', 'description']
admin.site.register(Experiences, ExperienceAdmin)

class ContactAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'email', 'message']
admin.site.register(Contact, ContactAdmin)