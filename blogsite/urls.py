from django.urls import path

from . import views

app_name = 'blogsite'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post', views.create_post, name='create_post'),
    path('get_post/<int:post_id>', views.get_post, name='get_post'),
]