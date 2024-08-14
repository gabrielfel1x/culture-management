from django.urls import path
from app_culture_management import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/<int:pk>/', views.detalhes_evento, name='detalhes_evento'),
    path('eventos/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/deletar/', views.deletar_evento, name='deletar_evento'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('perfil/', views.perfil, name='perfil'),
]
