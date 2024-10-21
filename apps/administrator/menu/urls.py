from django.urls import path
from apps.administrator.menu.views import MenuListView, MenuDetailView, MenuCreateView, MenuUpdateView, MenuDeleteView
urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('create/', MenuCreateView.as_view(), name='menu_create'),
    path('<int:pk>/', MenuDetailView.as_view(), name='menu_detail'),
    path('<int:pk>/update/', MenuUpdateView.as_view(), name='menu_update'),
    path('<int:pk>/delete/', MenuDeleteView.as_view(), name='menu_delete'),
]
