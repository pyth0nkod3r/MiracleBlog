from django.urls import path
from .views import (
    BlogappListView,
    BlogappDetailView,
    BlogappCreateView,
    BlogappUpdateView,
    BlogappDeleteView,
    )

urlpatterns = [
    path('', BlogappListView.as_view(), name='blogapphome'),
    path('post/<int:pk>/', BlogappDetailView.as_view(), name='blogappdetail'),
    path('post/new/', BlogappCreateView.as_view(), name='blogappcreatepost'),
    path('post/<int:pk>/edit/', BlogappUpdateView.as_view(), name='blogappupdate'),
    path('post/<int:pk>/delete/', BlogappDeleteView.as_view(), name='blogappdelete'),
]