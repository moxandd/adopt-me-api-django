from .models import Pet, Breed, PetAttachmentImage
from rest_framework import serializers

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['uuid', 'name', 'animal', 'breed', 'location', 'image', 'description', 'info']

class PetAttachmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetAttachmentImage
        fields = ['pet', 'image']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['animal', 'breeds']