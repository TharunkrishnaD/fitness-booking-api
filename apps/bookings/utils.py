import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'bookings_data.json')

def load_bookings():
    with open(FILE_PATH, 'r') as f:
        return json.load(f)

def save_booking(new_booking):
    bookings = load_bookings()
    bookings.append(new_booking)
    with open(FILE_PATH, 'w') as f:
        json.dump(bookings, f, indent=4)
