from django.contrib import admin

from .models import SiteInfo, About, Services

admin.site.register(SiteInfo)
admin.site.register(About)
admin.site.register(Services)