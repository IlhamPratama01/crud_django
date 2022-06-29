from django.urls import path

# import View dari todo Application
from .views import index_view, create_view, detail_view, update_view, delete_view

app_name = 'crud'
urlpatterns = [
    # route untuk halaman daftar task
    path('', index_view, name='index'),
    path('<int:task_id>', detail_view, name='detail'),
    path('create', create_view, name='create'),
     path('update/<int:task_id>', update_view, name='update'),
     path('delete/<int:task_id>', delete_view, name='delete'),

]