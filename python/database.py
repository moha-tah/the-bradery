import os
import mysql.connector
from dotenv import load_dotenv

from booking import Booking


MAIN_TABLE_NAME = 'Bookings'
NEW_TABLE_NAME = 'NewBookings'


class Database:
    def __init__(self):
        self.connection = self.db_connect()
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.db_disconnect()

    def db_connect(self):
        load_dotenv()

        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        # On vérifie que la connexion a bien été établie
        if connection.is_connected():
            print("Connecté à la bas de données MySQL.\n")
            return connection
        else:
            raise Exception("Erreur lors de la connexion à la base de données MySQL.")

    def db_disconnect(self):
        self.cursor.close()
        self.connection.close()
        print("\nDéconnecté de la base de données MySQL.")

    def booking_exists(self, booking_id: int, table_name: str) -> bool:
        request = f"SELECT * FROM {table_name} WHERE bookingId = {booking_id}"
        self.cursor.execute(request)

        return self.cursor.fetchone() is not None

    def get_booking_ids(self, table_name: str) -> list[int]:
        request = f"SELECT bookingId FROM {table_name}"
        self.cursor.execute(request)

        return [booking_id[0] for booking_id in self.cursor.fetchall()]

    def get_booking(self, booking_id: int, table_name: str) -> Booking:
        request = f"SELECT * FROM {table_name} WHERE bookingId = {booking_id}"
        self.cursor.execute(request)

        booking = self.cursor.fetchone()

        if booking:
            return Booking(booking_id=booking[0],
                           first_name=booking[1], last_name=booking[2],
                           total_price=booking[4], deposit_paid=booking[5],
                           check_in=booking[6], check_out=booking[7],
                           additional_needs=booking[8])
        else:
            # print(f"Réservation n°{booking_id} n'a pas été trouvé dans la table {MAIN_TABLE_NAME}.")
            return None

    def add_booking(self, booking: Booking, table_name: str = NEW_TABLE_NAME) -> None:
        if self.booking_exists(booking.booking_id, table_name):
            return
            # raise ValueError(f"La réservation n°{booking.booking_id} existe déjà dans la table {table_name}.")

        request: str = (f"INSERT INTO {table_name} "
                        "(bookingId, firstName, lastName, displayName, totalPrice, depositPaid, "
                        "checkIn, checkOut, additionalNeeds) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

        values: tuple = (booking.booking_id,
                         booking.first_name, booking.last_name, booking.display_name,
                         booking.total_price, booking.deposit_paid,
                         booking.check_in, booking.check_out,
                         booking.additional_needs)

        self.cursor.execute(request, values)

    def delete_booking(self, booking_id: int) -> None:
        # On supprime dans les deux tables pour être sûr

        request = f"DELETE FROM {MAIN_TABLE_NAME} WHERE bookingId = {booking_id}"
        self.cursor.execute(request)

        request = f"DELETE FROM {NEW_TABLE_NAME} WHERE bookingId = {booking_id}"
        self.cursor.execute(request)

    def delete_all_bookings(self):
        request = f"DELETE FROM {NEW_TABLE_NAME}"
        self.cursor.execute(request)
