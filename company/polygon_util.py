# polygon_util.py
import math

def is_point_in_polygon(coordinates, polygon_points):
    x, y = coordinates['lng'], coordinates['lat']
    n = len(polygon_points)
    is_inside = False
    for i in range(n):
        j = (i + 1) % n
        xi, yi = polygon_points[i]
        xj, yj = polygon_points[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            is_inside = not is_inside
    return is_inside

def get_distance_between_points(point1, point2):
    lat1, lon1 = point1['lat'], point1['lng']
    lat2, lon2 = point2['lat'], point2['lng']
    earth_radius_km = 6371.0  # Approximate radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius_km * c
    return distance