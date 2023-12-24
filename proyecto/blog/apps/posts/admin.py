from django.contrib import admin

# Register your models here.
from .models import Post, Categorias, Contacto


admin.site.register(Post)
admin.site.register(Categorias)
admin.site.register(Contacto)