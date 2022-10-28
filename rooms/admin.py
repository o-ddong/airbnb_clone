from django.contrib import admin

from rooms.models import Amenity, Room

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "kind", "owner", "created_at", "updated_at")
    list_filter = ("city", "price", "rooms", "toilets", "pet_friendly", "kind", "amenities")

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "created_at", "updated_at")