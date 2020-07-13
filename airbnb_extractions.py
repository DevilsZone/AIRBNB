import airbnb1
from auxiliary import property_check, add_new_property, extract_cities

api = airbnb1.Api(randomize=False, access_token="cx7b0gbrbvawl3ymyg20r428b")

def update_property(city_name, start_price=None, end_price=None):
    offset = 0
    while True:
        raw_data = api.get_homes(city_name, items_per_grid=50, offset=offset, priceMin=start_price, priceMax=end_price)
        is_paginated = raw_data['explore_tabs'][0]['pagination_metadata']['has_next_page']
        if len(raw_data['explore_tabs'][0]['sections']) == 1:
            try:
                listings = raw_data['explore_tabs'][0]['sections'][0]['listings']
            except KeyError as e:
                print(e.args)
                print([start_price, end_price])
                break
        else:
            listings = raw_data['explore_tabs'][0]['sections'][1]['listings']
        for listing in listings:
            if property_check(listing['listing']['id']):
                pass
            else:
                add_new_property(listing['listing'], listing['pricing_quote'], city_name)
        if is_paginated:
            offset += 50
        else:
            break


cities = extract_cities()
for city in cities:
    price_ranges = city.distribution.split('.')
    for ranges in price_ranges:
        start = int(ranges.split('-')[0])
        try:
            step = int(ranges.split('-')[1])
        except Exception as e:
            print(e.args)
            step = None
        try:
            end = int(ranges.split('-')[2])
        except Exception as e:
            print(e.args)
            end = None
        if step:
            if end:
                while start < end:
                    update_property(city.name, start, start+step)
                    start += step
            else:
                update_property(city.name, start)
        else:
            if end:
                update_property(city.name, start, end)
            else:
                update_property(city.name, start)
