
from django.urls import path

from .views import get, retrieve, update, post, delete

app_name = 'activos'

urlpatterns = [
    path('', get, name='get'),
    path('crear/', post, name='create'),
    path('<int:pk>/', update, name='update'),
    path('<int:pk>/detalle/', retrieve, name='detail'),
    path('<int:pk>/eliminar/', delete, name='delete'),
    
]
