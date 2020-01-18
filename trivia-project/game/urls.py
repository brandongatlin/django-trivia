from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='startpage'),
    path('gameboard/', views.gameboard, name='gameboard'),
    path('gameover/', views.gameover, name='gameover')
]