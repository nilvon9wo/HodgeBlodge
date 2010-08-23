from django.contrib import admin
from FluxHodgeBlodge.links.models import Link

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)

