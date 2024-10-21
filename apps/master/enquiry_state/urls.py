from django.urls import path
from .views import * 
urlpatterns = [
    path('', EnquiryStateListView.as_view(), name='enquiry_state_list'),
    path('create/', EnquiryStateCreateView.as_view(), name='enquiry_state_create'),
    # path('<int:pk>/', EnquiryStateDetailView.as_view(), name='enquiry_state_detail'),
    path('<int:pk>/update/', EnquiryStateUpdateView.as_view(), name='enquiry_state_update'),
    path('<int:pk>/delete/', EnquiryStateDeleteView.as_view(), name='enquiry_state_delete'),
]
