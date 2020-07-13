from django.contrib import admin
from .models import Country, City, Property
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class Country_Resource(resources.ModelResource):
    class Meta:
        model = Country

class Country_Admin(ImportExportModelAdmin):
    resource_class = Country_Resource


admin.site.register(Country, Country_Admin)


class City_Resource(resources.ModelResource):
    class Meta:
        model = City

class City_Admin(ImportExportModelAdmin):
    resource_class = City_Resource


admin.site.register(City, City_Admin)


class Property_Resource(resources.ModelResource):
    class Meta:
        model = Property

class Property_Admin(ImportExportModelAdmin):
    resource_class = Property_Resource


admin.site.register(Property, Property_Admin)
