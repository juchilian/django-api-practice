from django.urls import path
from .views import GetMenu, MenuView

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('menu/<str:menu_name>/', GetMenu.as_view()),
]