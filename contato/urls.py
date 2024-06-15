from django.urls import path
from contato import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/cliente<int:id>', views.showcontato,'cliente'),
    ]
