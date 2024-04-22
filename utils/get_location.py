locations = {
    'dhaka': {'lat': 23.7952, 'lon': 90.4162}, 
    'rajshahi': {'lat': 24.3736, 'lon': 88.6048}, 
    'khulna': {'lat': 22.8472, 'lon': 89.5367}, 
    'barishal': {'lat': 22.7111, 'lon': 90.3509}, 
    'mymensingh': {'lat': 24.7466, 'lon': 90.4155}, 
    'rangpur': {'lat': 25.749, 'lon': 89.2591}, 
    'chattogram': {'lat': 22.3757, 'lon': 91.8115}, 
    'sylhet': {'lat': 24.903, 'lon': 91.8648}
}

def get_location(city):
    data = locations[city] 
    return data['lat'], data['lon']