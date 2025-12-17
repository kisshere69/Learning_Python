import pandas
import csv

df = pandas.read_csv("hotels.csv", dtype={"id":str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self): #refer to a Hotel class

        """
        Book a hotel by changing its availability to 'no'
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


class Reservation_Ticket:
    def __init__(self, customer_name, hotel):
        pass
    def generate(self): #refer to a Hotel class
        pass


print(df)

hotel_id = input("Enter a hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available:
    hotel.book()
    customer_name = input("Enter your name: ")
    reservation_ticket = Reservation_Ticket(customer_name,hotel)
    reservation_ticket.generate()
else:
    print("Sorry, the hotel that you've selected is currently not available."
          "Don't worry, you can still select another hotel.")
