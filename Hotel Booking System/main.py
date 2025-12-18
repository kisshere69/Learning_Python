import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self): #refer to a Hotel class

        """
        Book a hotel by changing its availability to 'no' in the file
        """

        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    def available(self):

        """
        check if the id from .csv file = id from the user input
        """

        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self): #refer to a Hotel class
        content = f"""
        Thank you for your reservation!
        Here is your booking:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, full_name, cvc):
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "cvc": cvc,
            "holder": full_name
        }

        if card_data in df_cards:
            return True
        else:
            return False

print(df)

hotel_id = input("Enter a hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = CreditCard(number = "123456789123123")
    if credit_card.validate(expiration = "12/26", full_name = "JOHN SMITH", cvc = "123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name = name, hotel_object = hotel)
        print(reservation_ticket.generate())
    else:
        print("Sorry, your credit card is not valid.")
else:
    print("Sorry, the hotel that you've selected is currently not available."
          "Don't worry, you can still select another hotel.")