import pandas

"""Read data from .csv files"""

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)

"""Create a Hotel class"""

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    """Book a hotel by changing its availability to 'no' in the file"""

    def book(self): #refer to a Hotel class

        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    """Check if the id from .csv file = id from the user input"""

    def available(self):

        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

"""Create a ReservationTicket class"""

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self): #refer to a Hotel class
        content = f"""
        Thank you for choosing our hotel!
        
        Here is your booking:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content

"""Create a class for a spa ticket to inherit from ReservationTicket"""

class SpaTicket(ReservationTicket):
    def generate(self):
        content = f"""
        Thank you for choosing our spa! We look forward to seeing you soon.
        
        Here is your booking:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content

"""Create a CreditCard class"""

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


"""Child class of CreditCard to inherit its attributes and methods"""

class SecureCreditCard(CreditCard):

    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)

hotel_id = input("Enter a hotel id: ")
hotel = Hotel(hotel_id)

"""Main program"""

if hotel.available():
    credit_card = SecureCreditCard(number = "123456789123123")

    if credit_card.validate(expiration = "12/26", full_name = "JOHN SMITH", cvc = "123"):

        if credit_card.authenticate(given_password = "mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name = name, hotel_object = hotel)
            print(reservation_ticket.generate())

            spa = input("Would you like to book a spa session? (yes/no) ")

            if spa == "yes":
                spa_ticket = SpaTicket(customer_name = name, hotel_object = hotel)
                print(spa_ticket.generate())

            else:
                print(f"If you change your mind, please let us know."
                      f"\nHave a nice day and enjoy your stay, {name}!")

        else:
            print("Credit card authentication failed.")

    else:
        print("Sorry, your credit card is not valid.")

else:
    print("Sorry, the hotel that you've selected is currently not available. Please select another hotel.")