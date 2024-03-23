import csv
from api_find_geo.models import Location

def load_locations_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Location.objects.create(
                city=row['city'],
                state=row['state_id'],
                zip_code=row['zip'],
                latitude=float(row['lat']),
                longitude=float(row['lng'])
            )

def run():
    file_path = 'fixtures/uszips.csv'
    load_locations_from_csv(file_path)

if __name__ == '__main__':
    run()
