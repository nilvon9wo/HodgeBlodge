from django.contrib import admin
from models import TumbleItem

class TumbleItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(TumbleItem, TumbleItemAdmin)
