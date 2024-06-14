import os

from booking import Booking, input_booking
from database import Database, MAIN_TABLE_NAME, NEW_TABLE_NAME
from api import BookingAPI


def action_choice() -> int:
    print("\nQue souhaitez-vous faire ?")
    print("Table de base :")
    print("1 - Lister tous les IDs de réservation de la table de base.")
    print("2 - Afficher les informations d'une réservation de la table de base.\n")

    print("Nouvelle table :")
    print("3 - Lister les ID de réservation de la nouvelle table.")
    print("4 - Afficher les informations d'une réservation de la nouvelle table.")
    print("5 - Ajouter une réservation à la nouvelle table et à l'API.")
    print("6 - Supprimer une réservation de la nouvelle table et de l'API.")
    print("7 - Supprimer toutes les réservations de la nouvelle table et de l'API.")
    print("0 - Quitter le programme.")

    try:
        choice: int = int(input("Votre choix : "))
    except ValueError:
        print("Entrez un entier SVP.")
        return action_choice()

    if choice < 0 or choice > 7:
        print("Entrez un entier entre 0 et 7.")
        return action_choice()

    return choice


def main():
    db = Database()

    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")

    booking_api = BookingAPI(username, password)

    while True:
        choice = action_choice()

        print()

        if choice == 0:
            break

        elif choice == 1:
            print("IDs :", db.get_booking_ids(MAIN_TABLE_NAME))

        elif choice == 2:
            booking_id = int(input("Entrez l'ID de la réservation : "))
            if db.booking_exists(booking_id, MAIN_TABLE_NAME):
                print(db.get_booking(booking_id, MAIN_TABLE_NAME))
            else:
                print(f"La réservation n°{booking_id} n'existe pas dans la table {MAIN_TABLE_NAME}.")

        elif choice == 3:
            booking_ids = db.get_booking_ids(NEW_TABLE_NAME)
            if not booking_ids:
                print("Il n'y a aucune réservation dans la nouvelle table.")
            else:
                print(booking_ids)

        elif choice == 4:
            booking_id = int(input("Entrez l'ID de la réservation : "))
            if db.booking_exists(booking_id, NEW_TABLE_NAME):
                print(db.get_booking(booking_id, NEW_TABLE_NAME))
            else:
                print(f"La réservation n°{booking_id} n'existe pas dans la table {NEW_TABLE_NAME}.")

        elif choice == 5:
            booking = input_booking()

            # La fonction create_booking retourne l'ID de la réservation créée
            booking.booking_id = booking_api.create_booking(booking)

            print(f"Réservation n°{booking.booking_id} créée avec succès.\n")

            db.add_booking(booking)
            db.connection.commit()

        elif choice == 6:
            booking_id = int(input("Entrez l'ID de la réservation : "))
            if not db.booking_exists(booking_id, NEW_TABLE_NAME):
                print(f"La réservation n°{booking_id} n'existe pas dans la table {NEW_TABLE_NAME}.")
            else:
                booking_api.delete_booking(booking_id)
                db.delete_booking(booking_id)
                db.connection.commit()

        elif choice == 7:
            booking_ids = db.get_booking_ids(NEW_TABLE_NAME)

            for booking_id in booking_ids:
                booking_api.delete_booking(booking_id)

            db.delete_all_bookings()
            db.connection.commit()

            print("Toutes les réservations ont été supprimées de la nouvelle table et de l'API.")

    print("Fin du programme.")

if __name__ == '__main__':
    main()
