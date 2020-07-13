import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIRBNB.settings")
django.setup()

from backend.models import City, Property as P
from django.utils import timezone

def extract_cities():
    cities = City.objects.all()
    return cities


def property_check(prop_id):
    if P.objects.filter(prop_id=prop_id).exists():
        return True
    else:
        return False

def add_new_property(property_new, quote, default_city):
    prop_id = property_new['id']
    try:
        name = property_new['name']
    except Exception as e:
        print(e.args)
        name = None
    try:
        city = property_new['city']
    except Exception as e:
        print(e.args)
        city = default_city
    try:
        neighbour = property_new['neighborhood']
    except Exception as e:
        print(e.args)
        neighbour = None
    try:
        lat = property_new['lat']
    except Exception as e:
        print(e.args)
        lat = None
    try:
        long = property_new['lng']
    except Exception as e:
        print(e.args)
        long = None
    try:
        bed_rooms = property_new['bedrooms']
    except Exception as e:
        print(e.args)
        bed_rooms = None
    try:
        beds = property_new['beds']
    except Exception as e:
        print(e.args)
        beds = None
    try:
        bathrooms = property_new['bathrooms']
    except Exception as e:
        print(e.args)
        bathrooms = None
    try:
        lang = ", ".join(property_new['host_languages'])
    except Exception as e:
        print(e.args)
        lang = None
    try:
        capacity = property_new['person_capacity']
    except Exception as e:
        print(e.args)
        capacity = None
    try:
        addr = property_new['public_address']
    except Exception as e:
        print(e.args)
        addr = None
    try:
        amenities = ", ".join(property_new['amenity_ids'])
    except Exception as e:
        print(e.args)
        amenities = None
    try:
        room_type = property_new['room_type_category']
    except Exception as e:
        print(e.args)
        room_type = None
    try:
        guests = property_new['guest_label']
    except Exception as e:
        print(e.args)
        guests = None
    try:
        review = property_new['reviews_count']
    except Exception as e:
        print(e.args)
        review = 0
    try:
        star = property_new['star_rating']
    except Exception as e:
        print(e.args)
        star = 0
    try:
        avg_rat = property_new['avg_rating']
    except Exception as e:
        print(e.args)
        avg_rat = 0
    try:
        rate_type = quote['rate_type']
    except Exception as e:
        print(e.args)
        rate_type = None
    try:
        rate = quote['rate']['amount']
    except Exception as e:
        print(e.args)
        rate = 0
    try:
        currency = quote['rate']['currency']
    except Exception as e:
        print(e.args)
        currency = None
    try:
        price_data = quote['price_string']
        price = float(price_data.split(" ")[1][1:])
        price_curr = price_data.split(" ")[1][0]
    except Exception as e:
        print(e.args)
        price = 0
        price_curr = None
    try:
        min_night = property_new['min_nights']
    except Exception as e:
        print(e.args)
        min_night = 1
    try:
        cancel = property_new['cancel_policy']
    except Exception as e:
        print(e.args)
        cancel = None
    updated_at = timezone.now()
    property_added = P(prop_id=prop_id, prop_name=name, city=city, neighborhood=neighbour, latitude=lat, longitude=long,
                       bedrooms=bed_rooms, beds=beds, bathrooms=bathrooms, host_languages=lang, person_capacity=capacity
                       , public_address=addr, amenities=amenities, room_type_name=room_type, guest_label=guests,
                       review_count=review, star_rating=star, average_rating=avg_rat, rate_type=rate_type,
                       rate_amount=rate, rate_currency=currency, price_initial=price, price_initial_currency=price_curr,
                       min_nights=min_night, cancel_policy=cancel, updated_date=updated_at)
    try:
        property_added.save()
        print("{} added successfully.".format(name))
    except Exception as e:
        print(e.args)
