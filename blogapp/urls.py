from django.urls import path
from .views import BlogappListView, BlogappDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogappDetailView.as_view(), name='blogappdetail'),
    path('', BlogappListView.as_view(), name='blogapphome'),
]