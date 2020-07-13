from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(default='India', max_length=50)

    def __str__(self):
        return self.country


class City(models.Model):
    name = models.CharField(default='New Delhi', max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    distribution = models.CharField(default='0-None-500.501-None-', max_length=1000)

    def __str__(self):
        return self.name


class Property(models.Model):
    prop_id = models.BigIntegerField(unique=True, blank=False, null=False)
    prop_name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    neighborhood = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    bedrooms = models.SmallIntegerField(blank=True, null=True)
    beds = models.SmallIntegerField(blank=True, null=True)
    bathrooms = models.FloatField(blank=True, null=True)
    host_languages = models.CharField(max_length=255, blank=True, null=True)
    person_capacity = models.SmallIntegerField(blank=True, null=True)
    public_address = models.TextField(null=True, blank=True)
    amenities = models.TextField(max_length=1024, blank=True, null=True)
    room_type_name = models.CharField(max_length=255, null=True, blank=True)
    guest_label = models.CharField(max_length=255, null=True, blank=True)

    review_count = models.IntegerField(default=0, blank=True, null=True)
    star_rating = models.FloatField(default=0, blank=True, null=True)
    average_rating = models.FloatField(default=0, blank=True, null=True)
    location_rating = models.FloatField(default=0, blank=True, null=True)
    communication_rating = models.FloatField(default=0, blank=True, null=True)
    value_rating = models.FloatField(default=0, blank=True, null=True)
    check_in_rating = models.FloatField(default=0, blank=True, null=True)
    accuracy_rating = models.FloatField(default=0, blank=True, null=True)
    cleanliness_rating = models.FloatField(default=0, blank=True, null=True)

    rate_type = models.CharField(max_length=20, null=True, blank=True)
    rate_amount = models.FloatField(null=True, blank=True)
    rate_currency = models.CharField(max_length=255, blank=True, null=True)
    price_initial = models.FloatField(null=True, blank=True)
    price_initial_currency = models.CharField(max_length=255, blank=True, null=True)
    cleaning_fee = models.FloatField(max_length=10, null=True, blank=True)
    cleaning_fee_currency = models.CharField(max_length=255, blank=True, null=True)

    min_nights = models.SmallIntegerField(default=1, null=True, blank=True)
    cancel_policy = models.TextField(null=True, blank=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.prop_name + " | " + self.city
