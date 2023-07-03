from django.contrib import admin

from .models import Article, New, NewCategorie, Historie
admin.site.register(Article)
admin.site.register(New)
admin.site.register(NewCategorie)
admin.site.register(Historie)