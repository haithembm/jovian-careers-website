from django.urls import path
from . import views

app_name = 'careers'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/<int:pk>/apply/', views.job_apply, name='job_apply'),
    path('applications/<int:pk>/success/', views.apply_success, name='apply_success'),
]
