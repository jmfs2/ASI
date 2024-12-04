from django.db import models
from django.utils import timezone

class Defesa(models.Model):
    nome_motorista = models.CharField(max_length=100, default='')
    numero_infracao = models.CharField(max_length=50, default='')
    descricao = models.TextField(null=False, blank=False, default='')
    placa_veiculo = models.CharField(max_length=20, null=False, blank=False, default='')
    modelo_veiculo = models.CharField(max_length=100, default='', null=False, blank=False)
    ano_veiculo = models.IntegerField(default='', null=False, blank=False)
    local_infracao = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[('Em andamento', 'Em andamento'), ('Concluída', 'Concluída'), ('Rejeitada', 'Rejeitada')],
        default='Em andamento'
    )
    notificado = models.BooleanField(default=False)
    multa_id = models.CharField(max_length=100, null=False, blank=False)
    comentarios = models.TextField(null=True, blank=True)
    
    # Novo campo para CNPJ, que pode ser nulo
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    
    # Novo campo para o ID do agente de trânsito
    id_agente_transito = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Defesa {self.id} - {self.status}"

    class Meta:
        verbose_name = "Defesa"
        verbose_name_plural = "Defesas"
