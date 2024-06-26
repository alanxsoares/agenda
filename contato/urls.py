from django.urls import path
from contato import views

app_name = 'contato'
urlpatterns = [
    path('', views.index, name='index'),
    path('contato/<int:contato_id>/show', views.show_contato, name='show'),
    path('search/', views.search, name='search'),
    path('create/', views.add_contato, name='create'),
    path('contato/<int:pk>/update', views.up_contato, name='update'),

]
