from django.db import models
from django.urls import reverse
from django.core.validators import MaxLengthValidator, MinLengthValidator

from PIL import Image

class TeacherProfile(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False, )
    last_name = models.CharField(max_length=100, null=False, blank=False, )
    profile_picture = models.ImageField(null=True,)
    email_address = models.EmailField(null=False, blank=False, unique=True)
    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text="Required. 10 digits only. E.g 0552233444",
    )
    room_number = models.CharField(
        max_length=10, null=False, blank=False, 
        help_text="Class room number/letter combination like 4c",
    )
    subjects = models.CharField(max_length=1000, null=False, blank=False, )
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    
    def get_absolute_url(self):
        """Returns url to teacher profile page for updating and viewing"""
        return reverse("teacher_profile_detail", args = [str(self.id)]) 
