# setup/urls.py
from django.contrib import admin
from django.urls import path
from todos.views import home, registrar_defesa, consultar_defesa, sucesso  # Corrigido para importar de todos.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Agora, a view home será carregada corretamente
    path('registrar/', registrar_defesa, name='registrar_defesa'),
    path('consultar/', consultar_defesa, name='consultar_defesa'),
    path('sucesso/', sucesso, name='sucesso'),
]
