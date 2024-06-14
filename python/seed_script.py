import os
from dotenv import load_dotenv

from booking import Booking
from database import Database, MAIN_TABLE_NAME, NEW_TABLE_NAME
from api import BookingAPI


load_dotenv()

username = os.getenv("API_USERNAME")
password = os.getenv("API_PASSWORD")

db = Database()
booking_api = BookingAPI(username, password)

db.delete_all_bookings()

booking_ids = booking_api.get_booking_ids()
print(f"IDs des {len(booking_ids)} réservations : {booking_ids}")

for booking_id in booking_ids:
    print(f"Récupération de la réservation n°{booking_id}.", end=" ")

    booking = booking_api.get_booking(booking_id)

    if db.booking_exists(booking_id, MAIN_TABLE_NAME):
        print(f"La réservation n°{booking_id} existe déjà dans la table principale.")
        continue

    booking_api.create_booking(booking)
    db.add_booking(booking, MAIN_TABLE_NAME)
    db.connection.commit()

    print(f"La réservation n°{booking_id} a été ajoutée à la nouvelle table.")

print("\nToutes les réservations ont été ajoutées à la nouvelle table.")
