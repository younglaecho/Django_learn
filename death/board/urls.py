from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail), # <int:매개변수> views.board_detail의 매개변수에 해당 url 부분에 입력된 값을 입력한다.
    path('list/', views.board_list),
    path('write/', views.board_write)
]
