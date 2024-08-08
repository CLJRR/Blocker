import json
import csv

# File paths
manifest_path = 'manifest.json'
csv_path = './data/data.csv'

# Load manifest.json
with open(manifest_path, 'r') as f:
    manifest_data = json.load(f)

# Load URLs from CSV
urls = []
with open(csv_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        url = row.get('URL')  # Adjust the column name if necessary
        if url:
            urls.append(url + '/*')

# Add URLs to matches in manifest.json
matches = manifest_data['content_scripts'][0]['matches']
for url in urls:
    if url not in matches:
        matches.append(url)

# Save the updated manifest.json
with open(manifest_path, 'w') as f:
    json.dump(manifest_data, f, indent=4)

print("URLs have been added to manifest.json successfully.")