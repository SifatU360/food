from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

def food_donation_view(request):
    if request.method == 'POST':
        club_name = request.POST.get('club_name')
        food_item = request.POST.get('food_item')
        quantity = request.POST.get('quantity')

        # এখানে তুমি Model এ save করতে পারবে পরে
        print(f"Received: {club_name}, {food_item}, {quantity}")

        return HttpResponseRedirect('/')  # ফর্ম সাবমিট করার পর হোম পেজে পাঠিয়ে দিচ্ছি

    return render(request, 'food_delivery/food_donation_home.html')
