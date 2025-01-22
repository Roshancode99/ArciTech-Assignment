from django.urls import path
from .views import ContentItemListCreateAPIView, ContentItemRetrieveUpdateDestroyAPIView, AdminContentItemListAPIView, ContentItemSearchAPIView

urlpatterns = [
    path('content/', ContentItemListCreateAPIView.as_view(), name='content-list-create'),
    path('admin/content/', AdminContentItemListAPIView.as_view(), name='admin-content-list'),
    path('content/<int:pk>/', ContentItemRetrieveUpdateDestroyAPIView.as_view(), name='content-detail'),
    path('content/search/', ContentItemSearchAPIView.as_view(), name='content-search'),
]
