from django.urls import path
from .views import BlogListView, BlogCreateViews

app_name='blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateViews.as_view(), name='create')
]