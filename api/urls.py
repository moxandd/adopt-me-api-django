from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.PetsListApiView.as_view(), name='api-pets'),
    path('pets/<str:uuid>/', views.PetDetailView.as_view(), name='pet-detail'),
    path('breeds/', views.BreedsListApiView.as_view(), name='api-breeds'),
    path('pets_attachments/', views.PetAttachmentImagesListView.as_view(), name='pet-images')
]