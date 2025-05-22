from django.urls import path
from .views import LeadCreateView, LeadListView, LeadDetailView, LeadUpdateView

urlpatterns = [
    path('leads/', LeadCreateView.as_view(), name='lead-create'),
    path('leads-list/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('leads/<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
]
