from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'), path('Hposts/', views.Hposts, name='Hposts'), path('post/<str:num>', views.post, name='post'), path('Pposts/', views.Pposts, name='Pposts')
]
