from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main-index"),
    path('list/', views.list, name="main-list"),
]
