from django.db import models
from django.contrib.auth.models import User

class FoodClub(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class FoodDonation(models.Model):
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    donor_name = models.CharField(max_length=100)
    pickup_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    food_club = models.ForeignKey(FoodClub, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.food_name} by {self.donor_name}"

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username

class DeliveryTask(models.Model):
    food_club = models.ForeignKey(FoodClub, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='delivery_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Task for {self.food_club.name} by {self.volunteer.user.username}"
