from django.urls import path
from .views import HomePageView, AddPostView,PostDetailView
from . import views

app_name='feed'

urlpatterns=[
    path('', HomePageView.as_view(), name='index'),
    path('post/', AddPostView.as_view(), name='post'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
]
