from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.my_files, name='my_files'),
    path('<slug:subdir>/', views.my_files_subdir, name='my_files_subdir'),
]
