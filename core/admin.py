from django.contrib import admin

from core.models import Categoria, Editora, Livro, Autor

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)

