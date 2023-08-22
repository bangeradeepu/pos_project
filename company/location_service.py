# location_service.py
import http.client
import json
from .polygon_util import is_point_in_polygon, get_distance_between_points
from django.core.files.storage import default_storage
from .polygon_util import is_point_in_polygon, get_distance_between_points
from pos_project import constants

def get_location_details(coordinates, brand):
    in_polygon_promises = []
    nearest_outlet_promises = []

    brand_directory = f"companies/{brand}"
    outlets = default_storage.listdir(brand_directory)[1]

    for outlet_dir in outlets:
        settings_path = f"{brand_directory}/{outlet_dir}/{constants.LOCATION_FILES.LOCATION_SETTINGS}"

        if not default_storage.exists(settings_path):
            continue

        max_boundary = default_storage.open(settings_path).read()
        max_boundary = json.loads(max_boundary)['max_boundary']

        if is_point_in_polygon(coordinates, max_boundary):
            in_polygon_promises.append(
                create_in_polygon_promise(coordinates, outlet_dir, max_boundary)
            )

    for result in in_polygon_promises:
        settings_path = f"{brand_directory}/{result['outlet']}/{constants.LOCATION_FILES.LOCATION_SETTINGS}"
        if default_storage.exists(settings_path):
            outlet_origin = default_storage.open(settings_path).read()
            outlet_origin = json.loads(outlet_origin)['outlet_origin']

            nearest_outlet_promises.append(
                create_nearest_outlet_promise(coordinates, result['outlet'], outlet_origin)
            )

    nearest_outlet_promises.sort(key=lambda x: x['distance'])
    return nearest_outlet_promises

def create_in_polygon_promise(coordinates, outlet, max_boundary):
    if is_point_in_polygon(coordinates, max_boundary):
        return {
            'code': 200,
            'outlet': outlet,
        }
    return {'code': 400, 'outlet': outlet}

def create_nearest_outlet_promise(coordinates, outlet, outlet_origin):
    return {
        'code': 200,
        'outlet': outlet,
        'distance': get_distance_between_points(coordinates, outlet_origin),
    }



def get_distance_from_outlet(coordinates, outlet_coordinates):
    conn = http.client.HTTPSConnection("maps.googleapis.com")
    url = f"/maps/api/directions/json?origin={coordinates['lat']},{coordinates['lng']}&destination={outlet_coordinates['lat']},{outlet_coordinates['lng']}&key=YOUR_GOOGLE_MAPS_API_KEY"
    conn.request("GET", url)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    data_json = json.loads(data)
    return float(data_json['routes'][0]['legs'][0]['distance']['text'].replace(' km', ''))




def get_delivery_type_layers(coordinates, layers_settings):
    for layer in layers_settings:
        if is_point_in_polygon(coordinates, layer['coordinates']):
            return layer['charge_id']
    return None

def get_delivery_type_distance(coordinates, distances_settings, outlet_origin):
    distance = get_distance_from_outlet(coordinates, outlet_origin)
    sorted_distances = sorted(distances_settings, key=lambda x: x['distance'], reverse=True)
    for distance_item in sorted_distances:
        if distance <= distance_item['distance']:
            return distance_item['charge_id']
    return sorted_distances[0]['charge_id']

def init_delivery_type(location_settings, coordinates, layers_settings, distances_settings):
    if not is_point_in_polygon(coordinates, location_settings['max_boundary']):
        raise Exception("Location is outside the maximum delivery range")

    if location_settings['detection_type'] == 'LAYERS':
        if not layers_settings:
            raise Exception("Location setting needs to be updated (Layers)")
        return get_delivery_type_layers(coordinates, layers_settings)

    if not distances_settings:
        raise Exception("Location setting needs to be updated (Distances)")
    return get_delivery_type_distance(coordinates, distances_settings, location_settings['outlet_origin'])

def create_nearest_outlet_promise(coordinates, outlet, outlet_origin):
    distance = get_distance_between_points(coordinates, outlet_origin)
    return {
        'code': 200,
        'outlet': outlet,
        'distance': distance,
    }