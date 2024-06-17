from datetime import date


class Booking:
    def __init__(self, booking_id: int,
                 first_name: str, last_name: str,
                 total_price: int, deposit_paid: bool,
                 check_in: date, check_out: date,
                 additional_needs: str) -> None:

        self.booking_id: int = booking_id

        self.first_name: str = first_name
        self.last_name: str = last_name
        self.display_name: str = first_name + ' ' + last_name

        self.total_price: int = total_price  # total_price est un entier car, sur la documentation, c'est un entier
        self.deposit_paid: bool = deposit_paid

        self.check_in: date = check_in
        self.check_out: date = check_out

        if check_out < check_in:
            raise ValueError("La date de départ ne peut pas être avant la date d'arrivée.")

        self.additional_needs: str = additional_needs

    def __str__(self) -> str:
        pretty_check_in: str = self.check_in.strftime('%d/%m/%Y')
        pretty_check_out: str = self.check_out.strftime('%d/%m/%Y')

        res = (f"Réservation n°{self.booking_id} au nom de {self.display_name} :"
               f"\n   - Du {pretty_check_in} au {pretty_check_out}."
               f"\n   - Prix total : {self.total_price}$."
               f"\n   - Avance payée ? : {'Oui' if self.deposit_paid else 'Non'}."
               f"\n   - Besoins supplémentaires : {self.additional_needs}.")

        return res


def input_booking() -> Booking:
    first_name = input("Entrez le prénom : ")
    last_name = input("Entrez le nom : ")
    total_price = int(input("Entrez le prix de la réservation (int) : "))
    deposit_paid = input("L'avance a-t-elle été payée ? (Oui/Non) : ").lower() == 'oui'

    date_str = input("Entrez la date d'arrivée (JJ/MM/AAAA) : ")
    try:
        day, month, year = map(int, date_str.split('/'))
    except ValueError:
        print("Entrez une date d'arrivée valide SVP.")
        return input_booking()
    check_in = date(year, month, day)

    date_str = input("Entrez la date de départ (JJ/MM/AAAA) : ")
    try:
        day, month, year = map(int, date_str.split('/'))
    except ValueError:
        print("Entrez une date de départ valide SVP.")
        return input_booking()
    check_out = date(year, month, day)

    additional_needs = input("Entrez les besoins supplémentaires : ")

    return Booking(0, first_name, last_name, total_price, deposit_paid, check_in, check_out, additional_needs)
