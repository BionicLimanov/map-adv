from flask import Flask, request, send_file
from src import Gmaps
import csv

app = Flask(__name__)



@app.get('/get_data_image')
def get_data():
    search = str(request.args.get('queries'))
    modified_query = search.replace(" ", "_")
    queries = [search]
    max = int(request.args.get('max'))
    data = Gmaps.places(queries, max=max)
    csv_row = []
    # Define header for the CSV
    header = [
        "name", "address", "link", "main_category", "category", "is_spending_on_ads", "phones", "place_id", "rating", "review"
    ]

    for i in range(1, 8):  # Adjust the range according to the maximum number of best reviews
        header.extend([f"best_review_{i}_nama", f"best_review_{i}_rating", f"best_review_{i}_text", f"best_review_{i}_time"])

    # Write CSV file
    with open(f'{modified_query}.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(header)
        
        # Loop through each place and its best reviews
        for place_data in data:
            for place in place_data['places']:
                # Create a new row for each place
                row = [
                    place['name'],
                    place['address'],
                    place['link'],
                    place['main_category'],
                    ', '.join(place['categories']),
                    place['is_spending_on_ads'],
                    place['phoness'],
                    place['place_id'],
                    place['rating'],
                    place['reviews']
                ]
                
                # Append best review data
                for review in place['best_reviews']:
                    row.extend([
                        review['nama'],
                        review['rating'],
                        review['text'],
                        review['time']
                    ])
                
                # Write the row to the CSV file
                writer.writerow(row)
        
    # Return CSV file as response
    return send_file(f'{modified_query}.csv', as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)