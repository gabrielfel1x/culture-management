from django.urls import path
from app_culture_management import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/<int:pk>/', views.detalhes_evento, name='detalhes_evento'),
     path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/deletar/', views.deletar_evento, name='deletar_evento'),
]
