from src import Gmaps
import json
love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

class Category:
    Restaurant = "restaurant"
    Cafe = "cafe"
    Bar = "bar"
    Hotel = "hotel"
    BedAndBreakfast = "bed and breakfast"
    Hostel = "hostel"
    Supermarket = "supermarket"
    GroceryStore = "grocery store"
    Pharmacy = "pharmacy"
    Bank = "bank"
    ATM = "atm"
    GasStation = "gas station"
    Gym = "gym"
    Park = "park"
    Zoo = "zoo"
    Museum = "museum"
    Library = "library"
    School = "school"
    University = "university"
    Hospital = "hospital"
    Doctor = "doctor"
    Dentist = "dentist"
    VeterinaryCare = "veterinary care"
    CarRepair = "car repair"
    CarWash = "car wash"
    CarRental = "car rental"
    Airport = "airport"
    BusStation = "bus station"
    TrainStation = "train station"
    TaxiStand = "taxi stand"
    SubwayStation = "subway station"
    LightRailStation = "light rail station"
    BicycleStore = "bicycle store"
    HardwareStore = "hardware store"
    FurnitureStore = "furniture store"
    ElectronicsStore = "electronics store"
    ClothingStore = "clothing store"
    ShoeStore = "shoe store"
    JewelryStore = "jewelry store"
    BookStore = "book store"
    Florist = "florist"
    DepartmentStore = "department store"
    ShoppingMall = "shopping mall"
    MovieTheater = "movie theater"
    BowlingAlley = "bowling alley"
    Stadium = "stadium"
    Aquarium = "aquarium"
    AmusementPark = "amusement park"


# Baca data dari file indonesia.json
with open('indonesia.json') as f:
    data = json.load(f)

# Ambil daftar kabupaten yang berbeda
unique_kabupaten = set(item["KABUPATEN"] for item in data)

for kabupaten in unique_kabupaten:
   # Mengambil semua atribut dari kelas Category
   category_values = vars(Category).values()

   # Loop melalui setiap nilai dan membuat permintaan
   for category in category_values:
        query = f"{category} in {kabupaten}"
        try:
            # Mencari tempat menggunakan Google Maps API
            places = Gmaps.places([query], max=150)

            # Cetak hasil pencarian
            for place in places:
                print(place)  # Anda mungkin ingin menyesuaikan bagaimana informasi tempat ini dicetak
        except Exception as e:
            print(f"Error while searching places: {e}")
