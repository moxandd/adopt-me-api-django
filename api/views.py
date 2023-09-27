from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import PetSerializer, BreedSerializer, PetAttachmentImageSerializer
from .models import Pet, Breed, PetAttachmentImage
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class PetsListApiView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('name', 'animal', 'location', 'breed')
    search_fields = ('name', 'animal', 'location', 'breed')

class PetDetailView(generics.RetrieveAPIView):
    lookup_field = "uuid"
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetAttachmentImagesListView(generics.ListAPIView):
    queryset = PetAttachmentImage.objects.all()
    serializer_class = PetAttachmentImageSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('pet',)
    search_fields = ('pet',)

class BreedsListApiView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('animal',)
    search_fields = ('animal',)
