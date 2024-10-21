from django.urls import path
from .views import *
urlpatterns = [
    path('', CountryListView.as_view(), name='country_list'),
    path('create/', CountryCreateView.as_view(), name='country_create'),
    # path('<int:pk>/', CountryDetailView.as_view(), name='master_action_taken_detail'),
    path('<int:pk>/update/', CountryUpdateView.as_view(), name='master_country_update'),
    path('<int:pk>/delete/', CountryDeleteView.as_view(), name='master_country_delete'),
]
