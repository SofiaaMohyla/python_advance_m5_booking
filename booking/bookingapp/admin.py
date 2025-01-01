from django.contrib import admin

from .models import Category, Room, Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "room", "check_in", "check_out", "phone", "creation_time")
    list_display_links = ("id", "client", "room", "check_in", )



admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)

