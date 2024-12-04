from django import forms
from .models import Defesa

class RegistrarDefesaForm(forms.ModelForm):
    class Meta:
        model = Defesa
        fields = ['nome_motorista', 'numero_infracao', 'descricao', 'placa_veiculo', 'modelo_veiculo', 'ano_veiculo', 'local_infracao', 'status', 'notificado', 'multa_id', 'comentarios', 'cnpj', 'id_agente_transito']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'comentarios': forms.Textarea(attrs={'rows': 3}),
        }

class ConsultarDefesaForm(forms.Form):
    numero_infracao = forms.CharField(max_length=50, required=False, label='Número da Infração')
    placa_veiculo = forms.CharField(max_length=20, required=False, label='Placa do Veículo')
    cnh = forms.CharField(max_length=20, required=False, label='CNH')
    cpf = forms.CharField(max_length=20, required=False, label='CPF')
    multa_id = forms.CharField(max_length=100, required=False, label='ID da Multa')
    cnpj = forms.CharField(max_length=20, required=False, label='CNPJ')
    id_agente_transito = forms.CharField(max_length=50, required=False, label='ID do Agente')

    # O campo de status pode ser opcional, caso seja necessário filtrar por status
    status = forms.ChoiceField(
        choices=[('Em andamento', 'Em andamento'), ('Concluída', 'Concluída'), ('Rejeitada', 'Rejeitada')],
        required=False, label='Status'
    )