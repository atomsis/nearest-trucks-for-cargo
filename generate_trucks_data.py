import csv
import json
import random
from django.core.management import call_command


def read_locations_from_csv(file_path):
    locations = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            locations.append({
                'city': row['city'],
                'state': row['state_id'],
                'zip_code': row['zip'],
                'latitude': float(row['lat']),
                'longitude': float(row['lng'])
            })
    return locations


def generate_trucks_data(locations, num_trucks=20):
    trucks = []
    for i in range(1, num_trucks + 1):
        truck = {
            'model': 'api_find_geo.Truck',
            'pk': i,
            'fields': {
                'unique_number': f"{random.randint(1000, 9999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
                'current_location': random.randint(1, len(locations)),
                'capacity': random.randint(1, 1000)
            }
        }
        trucks.append(truck)
    return trucks


def save_to_json(data, file_path):
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def main():
    locations = read_locations_from_csv('uszips.csv')

    trucks_data = generate_trucks_data(locations)

    save_to_json(trucks_data, 'initial_data.json')

    call_command('loaddata', 'initial_data.json')


if __name__ == "__main__":
    main()
