from django.db import models
import uuid

# Create your models here.

class Pet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=150, default="Unnamed")
    animal = models.CharField(max_length=150, default="")
    breed = models.CharField(max_length=150, default="")
    location = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='images/pet.png', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    info = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.animal} - {self.name} - {self.breed}"
    
class PetAttachmentImage(models.Model):
    pet = models.ForeignKey(Pet, to_field='uuid', on_delete=models.CASCADE, related_name="pet")
    image = models.ImageField(upload_to='images/pet_attachments_images/', blank=False, null=False)
    
class Breed(models.Model):
    animal = models.CharField(max_length=100, blank=False, null=False)
    breeds = models.CharField(max_length=800, blank=False, null=False)

    def __str__(self):
        return f"{self.animal}'s breeds" 
    
