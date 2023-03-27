from django.urls import path
from chamada.views import index

urlpatterns = [
    path('', index, name='chamada')
]