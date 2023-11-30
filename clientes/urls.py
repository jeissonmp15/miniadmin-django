
from django.urls import path

from .views import get, retrieve, update, post, delete

app_name = 'clientes'

urlpatterns = [
    path('', get, name='get'),
    path('crear/', post, name='create'),
    path('<int:cliente_id>/', update, name='update'),
    path('<int:cliente_id>/detalle/', retrieve, name='detail'),
    path('<int:cliente_id>/eliminar/', delete, name='delete'),
    
]
