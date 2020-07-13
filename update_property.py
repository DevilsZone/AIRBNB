import airbnb1

api = airbnb1.Api(randomize=True, access_token="cx7b0gbrbvawl3ymyg20r428b")

for i in range(1):
    x = api.get_homes("New Delhi, Delhi", items_per_grid=50, offset=0, priceMin=10, priceMax=100)
    if len(x['explore_tabs'][0]['sections']) == 1:
        y = x['explore_tabs'][0]['sections'][0]['listings']
    else:
        y = x['explore_tabs'][0]['sections'][1]['listings']
    for j in y:
        print("City = {}, id = {}\n".format(j['listing']['city'], j['listing']['id']))

next_exists = x['explore_tabs'][0]['pagination_metadata']['has_next_page']
