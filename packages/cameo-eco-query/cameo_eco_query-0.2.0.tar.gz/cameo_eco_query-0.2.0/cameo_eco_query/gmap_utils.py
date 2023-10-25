import geocoder

def get_gmap_url(location, google_key):
    location_data = geocoder.google(location, key=google_key).json
    return f'https://www.google.com.tw/maps/search/{location_data["lat"]},{location_data["lng"]}'
