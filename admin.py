from django.contrib import admin
from FluxHodgeBlodge.blog.models import Blog
from FluxHodgeBlodge.blog.admin import BlogAdmin
from FluxHodgeBlodge.links.models import Link
from FluxHodgeBlodge.links.admin import LinkAdmin
from FluxHodgeBlodge.tumblelog.models import TumbleItem
from FluxHodgeBlodge.tumblelog.admin import TumbleItemAdmin


class AdminSite (admin.AdminSite):
    pass

site = AdminSite()

site.register(Blog, BlogAdmin)
site.register(Link, LinkAdmin)
site.register(TumbleItem, TumbleItemAdmin)
