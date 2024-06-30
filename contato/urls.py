from django.urls import path
from contato import views

app_name = 'contato'
urlpatterns = [
    path('', views.index, name='index'),
    path('contato/<int:contato_id>/show', views.show_contato, name='show'),
    path('search/', views.search, name='search'),
    path('create/', views.add_contato, name='create'),
    path('contato/<int:pk>/update', views.up_contato, name='update'),
    path('contato/<int:pk>/delete', views.del_contato, name='delete'),
    path('user/create', views.user_create, name='create_user'),
    path('user/login/', views.user_login, name='login'),
    path('user/logout/', views.user_logout, name='logout')

]
