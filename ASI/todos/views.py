from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Defesa
from .forms import RegistrarDefesaForm, ConsultarDefesaForm

# View para a página inicial
def home(request):
    return render(request, 'home.html')
# View para registrar defesa
def registrar_defesa(request):
    if request.method == 'POST':
        form = RegistrarDefesaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a defesa e as datas são atribuídas automaticamente
            return redirect('sucesso')  # Redireciona para a página de sucesso
        else:
            # Se o formulário for inválido, mostra os erros
            return render(request, 'registrar_defesa.html', {'form': form})
    else:
        form = RegistrarDefesaForm()  # Cria um formulário vazio
    return render(request, 'registrar_defesa.html', {'form': form})

# View para consultar defesa
def consultar_defesa(request):
    form = ConsultarDefesaForm(request.GET or None)
    defesas = []

    if form.is_valid():
        # Pega os dados dos campos do formulário
        numero_infracao = form.cleaned_data.get('numero_infracao')
        placa_veiculo = form.cleaned_data.get('placa_veiculo')
        cnh = form.cleaned_data.get('cnh')
        cpf = form.cleaned_data.get('cpf')
        multa_id = form.cleaned_data.get('multa_id')
        cnpj = form.cleaned_data.get('cnpj')
        id_agente_transito = form.cleaned_data.get('id_agente_transito')
        status = form.cleaned_data.get('status')

        # Inicia a queryset para filtrar as defesas
        defesas = Defesa.objects.all()

        # Aplica os filtros conforme o que foi preenchido no formulário
        if numero_infracao:
            defesas = defesas.filter(numero_infracao=numero_infracao)
        if placa_veiculo:
            defesas = defesas.filter(placa_veiculo=placa_veiculo)
        if cnh:
            defesas = defesas.filter(cnh=cnh)
        if cpf:
            defesas = defesas.filter(cpf=cpf)
        if multa_id:
            defesas = defesas.filter(multa_id=multa_id)
        if cnpj:
            defesas = defesas.filter(cnpj=cnpj)
        if id_agente_transito:
            defesas = defesas.filter(id_agente_transito=id_agente_transito)
        if status:
            defesas = defesas.filter(status=status)

    return render(request, 'consultar_defesa.html', {'form': form, 'defesas': defesas})

# View para página de sucesso após registrar defesa
def sucesso(request):
    return render(request, 'sucesso.html')