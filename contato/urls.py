from django.urls import path
from contato import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/<int:contato_id>/', views.show_contato, name='show')
]
