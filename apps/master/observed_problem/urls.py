from django.urls import path
from .views import *
urlpatterns = [
    path('', ObservedProblemListView.as_view(), name='observed_problem_list'),
    path('create/', ObservedProblemCreateView.as_view(), name='observed_problem_create'),
    # path('<int:pk>/', ObservedProblemDetailView.as_view(), name='observed_problem_detail'),
    path('<int:pk>/update/', ObservedProblemUpdateView.as_view(), name='observed_problem_update'),
    path('<int:pk>/delete/', ObservedProblemDeleteView.as_view(), name='observed_problem_delete'),
]
