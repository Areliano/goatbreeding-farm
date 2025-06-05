from django.contrib import admin

# Register your models here.

from .models import Homepage, About, Founder

admin.site.register(Homepage)

admin.site.register(About)

admin.site.register(Founder)
