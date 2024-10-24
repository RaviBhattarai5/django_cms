from django.urls import path
from .views import * 
urlpatterns = [
    path('', EnquiryStatusListView.as_view(), name='enquire_status_list'),
    path('create/', EnquiryStatusCreateView.as_view(), name='enquire_status_create'),
    # path('<int:pk>/', EnquiryStatusDetailView.as_view(), name='enquire_status_detail'),
    path('<int:pk>/update/', EnquiryStatusUpdateView.as_view(), name='enquire_status_update'),
    path('<int:pk>/delete/', EnquiryStatusDeleteView.as_view(), name='enquire_status_delete'),
]
