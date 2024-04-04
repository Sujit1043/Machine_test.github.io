from django.urls import path
from . import views
from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView, ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView

urlpatterns = [
    
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-retrieve-update-destroy'),
]
