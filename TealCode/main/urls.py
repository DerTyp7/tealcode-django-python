from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main-index"),
    path('topic/<str:category>/<str:topic>/', views.topic, name="main-topic"),
    path('category/<str:category>/', views.category, name="main-category"),
    path('about/', views.about, name="main-about"),
    path('privacy/', views.privacy, name="main-privacy"),
    path('search/<str:value>/', views.search, name="main-search"),
    path('sitemap.xml', views.sitemap, name="main-sitemap"),
]
