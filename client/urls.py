from django.urls import path
from . import views


#=== ALL MY URLS ===|
urlpatterns = [
    path('', views.index, name='index'),
    path('washcount/<int:client_id>/', views.wash_count, name='wash_count'),
    path('reset/<int:client_id>/', views.reset_wash_count, name='reset_count'),
]