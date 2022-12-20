import json
import csv
import boto3
import colorsys


def handler_color(event, context):

    # Pobieramy listę plików csv z folderu csv-files w buckecie csv-bucket
    s3 = boto3.client('s3')
    bucket_name = 'csv-bucket'
    prefix = 'csv-files/'
    file_names = ['example.csv', 'example1.csv', 'example2.csv']

    # Pobieramy zawartość plików csv i tworzymy listę słowników z danymi o kolorach
    color_data = []
    for file_name in file_names:
        csv_content = s3.get_object(Bucket=bucket_name, Key=f'{prefix}{file_name}')['Body'].read().decode()
        reader = csv.DictReader(csv_content.splitlines())
        for row in reader:
            color_hex = row['value']
            r, g, b = colorsys.hex_to_rgb(color_hex)
            color_data.append({
                'name': row['color'],
                'hex': color_hex,
                'rgb': [r, g, b]
            })

    # Tworzymy plik json z danymi o kolorach i zapisujemy go do bucket'u
    json_data = json.dumps(color_data)
    s3.put_object(Bucket=bucket_name, Key='json-files/colors.json', Body=json_data)

    # Wyświetlamy dostępną paletę kolorów
    print('Dostępna paleta kolorów:')
    for color in color_data:
        print(f'{color["name"]}: #{color["hex"]} ({color["rgb"]})')

    return len(color_data)