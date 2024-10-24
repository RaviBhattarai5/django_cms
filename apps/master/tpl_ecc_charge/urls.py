from django.urls import path
from . views import *
urlpatterns = [
    path('', TcpEccChargeListView.as_view(), name='tpl_ecc_charge_list'),
    path('create/', TcpEccChargeCreateView.as_view(), name='tpl_ecc_charge_create'),
    # path('<int:pk>/', TcpEccChargeUpdateView.as_view(), name='tcp_ecc_charge_detail'),
    path('<int:pk>/update/', TcpEccChargeUpdateView.as_view(), name='tpl_ecc_charge_update'),
    path('<int:pk>/delete/', TcpEccChargeDeleteView.as_view(), name='tpl_ecc_charge_delete'),
]
