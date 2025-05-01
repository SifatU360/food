from django.contrib import admin
from django.urls import path
from food_delivery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('donate/', views.food_donation_view, name='food_donation'),
    path('foodclub/<int:club_id>/', views.food_club_profile, name='food_club_profile'),
    path('foodclub/barishal/', views.food_club_profile, {'club_id': 1}, name='barishal_food_club_profile'),
    path('foodclub/foodking/', views.food_club_profile, {'club_id': 2}, name='food_king_food_club_profile'),
    path('foodclub/pizzacompany/', views.food_club_profile, {'club_id': 3}, name='pizza_company_food_club_profile'),
]
