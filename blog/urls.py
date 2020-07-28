from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'), path('posts/', views.posts, name='posts'), path('post/<str:name>', views.post, name='post')
]
