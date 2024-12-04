# Register your models here.
from django.contrib import admin
from .models import Defesa

class DefesaAdmin(admin.ModelAdmin):
    list_display = ('nome_motorista', 'numero_infracao', 'status', 'placa_veiculo', 'modelo_veiculo', 'comentarios', 'cnpj', 'id_agente_transito')
    search_fields = ('nome_motorista', 'numero_infracao', 'placa_veiculo', 'cnpj')  # Incluindo cnpj na busca
    list_filter = ('status',)

admin.site.register(Defesa, DefesaAdmin)
