from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main-index"),
    path('topic/<str:category>/<str:topic>/', views.topic, name="main-topic"),
    path('category/<str:category>/', views.category, name="main-category"),
]
