from django.contrib import admin

from pessoas.models import Pessoa, Telefone

admin.site.register(Pessoa)
admin.site.register(Telefone)