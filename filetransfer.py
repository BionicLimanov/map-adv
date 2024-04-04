import json
from src import Gmaps
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("GoogleMapsScraper") \
    .getOrCreate()

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

class Category:
    Zoo = "zoo"

# Read data from indonesia.json
with open('indonesia2.json') as f:
    data = json.load(f)

# Extract unique kabupaten (districts)
unique_kabupaten = set(item["KABUPATEN"] for item in data)

# Create Spark DataFrame to store results
columns = ["Name", "Address", "Latitude", "Longitude"]
results = []

for kabupaten in unique_kabupaten:
    category_values = vars(Category).values()

    for category in category_values:
        query = f"{category} in {kabupaten}"
        try:
            # Search for places using Google Maps API
            places = Gmaps.places([query], max=150)

            # Store the results
            for place in places:
                results.append((place.name, place.address, place.lat, place.lng))
        except Exception as e:
            print(f"Error while searching places: {e}")

# Create RDD from results
rdd = spark.sparkContext.parallelize(results)

# Convert RDD to DataFrame
df = rdd.map(lambda x: Row(Name=x[0], Address=x[1], Latitude=x[2], Longitude=x[3])).toDF(columns)

# Write DataFrame to Hadoop as CSV file
df.write.mode('overwrite').csv("hdfs:///path/to/your/csv/file")

# Stop SparkSession
spark.stop()
