from django.contrib import admin
from .models import FoodDonation, FoodClub, Volunteer, DeliveryTask

@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'quantity', 'donor_name', 'pickup_address', 'created_at')
    search_fields = ('food_name', 'donor_name')
    list_filter = ('created_at',)

@admin.register(FoodClub)
class FoodClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)
    list_filter = ('location',)

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number')

@admin.register(DeliveryTask)
class DeliveryTaskAdmin(admin.ModelAdmin):
    list_display = ('food_club', 'volunteer', 'description', 'completed', 'created_at', 'completed_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('food_club__name', 'volunteer__user__username')