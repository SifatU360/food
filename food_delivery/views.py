from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from food_delivery.models import FoodDonation, FoodClub

def home(request):
    return HttpResponse("Welcome to Food Redistribution Project!")

def food_donation_view(request):
    food_clubs = FoodClub.objects.all()
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        quantity = request.POST.get('quantity')
        donor_name = request.POST.get('donor_name')
        pickup_address = request.POST.get('pickup_address')
        food_club_id = request.POST.get('food_club')

        food_club = None
        if food_club_id:
            food_club = get_object_or_404(FoodClub, id=food_club_id)

        # Save the donation to the database
        donation = FoodDonation(
            food_name=food_name,
            quantity=quantity,
            donor_name=donor_name,
            pickup_address=pickup_address,
            food_club=food_club
        )
        donation.save()

        return HttpResponseRedirect('/')  # Redirect to home page after submission

    return render(request, 'food_donation.html', {'food_clubs': food_clubs})

def food_club_profile(request, club_id):
    food_club = get_object_or_404(FoodClub, id=club_id)
    donations = FoodDonation.objects.filter(food_club=food_club).order_by('-created_at')
    return render(request, 'food_club_profile.html', {'food_club': food_club, 'donations': donations})
