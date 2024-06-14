import requests

from booking import Booking


BASE_URL = "https://restful-booker.herokuapp.com/"


class BookingAPI:
    def __init__(self, username: str, password: str):
        self.username: str = username
        self.password: str = password

        # On stocke le token car il peut servir pour certaines requêtes comme le delete.
        self.token: str = self.get_token_from_api()

    def get_token_from_api(self) -> str:
        response = requests.post(BASE_URL + "auth",
                                 json={"username": self.username,
                                       "password": self.password})

        if response.status_code != 200:
            raise Exception(f"Erreur lors de la récupération du token : {response.text}")

        return response.json()["token"]

    def get_booking_ids(self) -> list[int]:
        response = requests.get(BASE_URL + "booking")

        if response.status_code != 200:
            raise Exception(f"Erreur lors de la récupération des IDs de réservation : {response.text}")

        # On formate le json en une liste d'IDs de réservation
        return [booking["bookingid"] for booking in response.json()]

    def get_booking(self, booking_id: int) -> Booking:
        response = requests.get(BASE_URL + f"booking/{booking_id}")

        if response.status_code != 200:
            raise Exception(f"Erreur lors de la récupération de la réservation {booking_id} : {response.text}")

        res = response.json()

        if "additionalneeds" not in res:
            res["additionalneeds"] = ""

        # On formate le json en un objet Booking
        return Booking(booking_id,
                       res["firstname"], res["lastname"],
                       res["totalprice"], res["depositpaid"],
                       res["bookingdates"]["checkin"], res["bookingdates"]["checkout"],
                       res["additionalneeds"])

    def create_booking(self, booking: Booking) -> int:
        response = requests.post(BASE_URL + "booking",
                                 json={"firstname": booking.first_name,
                                       "lastname": booking.last_name,
                                       "totalprice": booking.total_price,
                                       "depositpaid": booking.deposit_paid,
                                       "bookingdates": {"checkin": str(booking.check_in),
                                                        "checkout": str(booking.check_out)},
                                       "additionalneeds": booking.additional_needs},
                                 headers={"Content-Type": "application/json",
                                          "Accept": "application/json",
                                          "Cookie": f"token={self.token}"})

        if response.status_code != 200:
            raise Exception(f"Erreur lors de la création de la réservation : {response.text}")

        # L'API renvoie un json avec l'ID de la réservation créée
        booking_id: int = response.json()["bookingid"]

        # print(f"Réservation n°{booking_id} créée avec succès.")

        return booking_id

    def delete_booking(self, booking_id: int) -> None:
        try:
            self.get_booking(booking_id)
        except Exception as e:
            print(f"La réservation n°{booking_id} n'existe pas.")
            return

        response = requests.delete(BASE_URL + f"booking/{booking_id}",
                                   headers={"Cookie": f"token={self.token}"})

        if response.status_code != 201:
            raise Exception(f"Erreur lors de la suppression de la réservation {booking_id} : {response.text}")

        print(f"Réservation n°{booking_id} supprimée avec succès.")
